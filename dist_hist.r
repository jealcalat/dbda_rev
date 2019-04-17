dist_hist <- function(dist,
                      pars,
                      xlab = 'x',
                      color = 'grey60',
                      bootci = TRUE,
                      den = FALSE,
                      border = FALSE){
  
  if(is.character(dist)){
    if(dist == 'norm'){
      x = rnorm(pars[1],pars[2],pars[3])
    } else if( dist == 'exp'){
      x = rexp(pars[1],pars[2])
    } else if( dist == 'F'){
      x = rf(pars[1],pars[2],pars[3])
    } 
  } else {
    x = dist
  }
  
  if(bootci){
    B = 1000 #número de bootstraps
    N = length(x) #longitud de vector de datos
    boot_vec = numeric(B) #para guardar resultados
    for(b in 1:B){ #boostrap
      # sample toma N valores de x con reemplazo
      bsample = sample(x,size = N, replace = T)
      # obtener un estadístico
      boot_vec[b] <- mean(bsample)
    }
    # para conocer los intervalos de confianza 
    lw = quantile(boot_vec,probs = 0.025)
    up = quantile(boot_vec,probs = 0.975)
    center = mean(boot_vec)
  } else { # iqr
    lw = quantile(x,probs = 0.25)
    up = quantile(x,probs = 0.75)
    center = median(x)
  }
  
  
  if(border == F) border = color
  par(mgp = c(2,0.3,0))
  # guardar  
  h = hist(x,breaks = 'fd',plot = F)
  max.y = max(h$density)
  plot(h,col = color, border = border,
       ylim = c(0,max.y*1.1),
       axes = F,ylab = '',xlab = xlab,
       freq = F,main = '')
  points(x = center,y = max.y*1.05, pch = '+',col = color,cex = 2)
  segments(x0 = lw,x1 = up,y0 = max.y*1.05,y1 = max.y*1.05)
  segments(x0 = lw,x1 = lw,y0 = max.y*1.03,y1 = max.y*1.07)
  segments(x0 = up,x1 = up,y0 = max.y*1.03,y1 = max.y*1.07)
  
  axis(1,tck = -0.01, las = 1)
  if(den == TRUE){
    dx = density(x,adjust = 2)
    lines(dx, col = 'black')
  }
}

# Normal
dist_hist('norm',pars = c(1000,10,1.2),bootci = F,den = T,xlab = 'Normal',color = 'steelblue',border = F)
legend('topleft',legend = bquote(N(mu,sigma)),bty = 'n')
# Exponencial
dist_hist('exp',pars = c(1000,1/60),bootci = F,den = T,xlab = 'Exp',color = 'red4',border = F)
# F
dist_hist('F',pars = c(1000,6,32),bootci = F,den = T,xlab = 'Fdist',color = "slateblue1"  ,border = F)
# Datos propios (supongamos otra distibucion)
d = rbinom(1000,40,0.3)

dist_hist(d,bootci = F,den = T,xlab = 'Data',color = 'slateblue1',border = F)
# se pueden agregar más elemengos
abline(v = 12)
axis(2,tck = -0.01, las = 2,labels = F)
legend('topleft',legend = bquote(Binom(p,k)))
box()
