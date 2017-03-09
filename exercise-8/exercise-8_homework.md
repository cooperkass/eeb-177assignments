Example Data--Housing
---------------------

### Histograms--Base vs. ggplot2

    housing <- read.csv("/home/eeb177-student/Desktop/eeb-177/lab-work/exercise-8/Rgraphics/dataSets/landdata-states.csv")
    head(housing[1:5])

    ##   State region    Date Home.Value Structure.Cost
    ## 1    AK   West 2010.25     224952         160599
    ## 2    AK   West 2010.50     225511         160252
    ## 3    AK   West 2009.75     225820         163791
    ## 4    AK   West 2010.00     224994         161787
    ## 5    AK   West 2008.00     234590         155400
    ## 6    AK   West 2008.25     233714         157458

    hist(housing$Home.Value)
    library(ggplot2)

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-1-1.png)

    ggplot(housing, aes(x = Home.Value)) +
      geom_histogram()

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-1-2.png)

### Scatter plots--Base vs. ggplot2

    plot(Home.Value ~ Date,
         data=subset(housing, State == "MA"))
    points(Home.Value ~ Date, col="red",
           data=subset(housing, State == "TX"))
    legend(1975, 400000,
           c("MA", "TX"), title="State",
           col=c("black", "red"),
           pch=c(1, 1))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-2-1.png)

    ggplot(subset(housing, State %in% c("MA", "TX")),
           aes(x=Date,
               y=Home.Value,
               color=State))+
      geom_point()

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-2-2.png)

Geometric Objects and Aethetics
-------------------------------

    hp2001Q1 <- subset(housing, Date == 2001.25) 
    ggplot(hp2001Q1,
           aes(y = Structure.Cost, x = Land.Value)) +
      geom_point()

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-3-1.png)

    ggplot(hp2001Q1,
           aes(y = Structure.Cost, x = log(Land.Value))) +
      geom_point()

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-4-1.png)

    hp2001Q1$pred.SC <- predict(lm(Structure.Cost ~ log(Land.Value), data = hp2001Q1))

    p1 <- ggplot(hp2001Q1, aes(x = log(Land.Value), y = Structure.Cost))

    p1 + geom_point(aes(color = Home.Value)) +
      geom_line(aes(y = pred.SC))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-5-1.png)

    p1 +
      geom_point(aes(color = Home.Value)) +
      geom_smooth()

    ## `geom_smooth()` using method = 'loess'

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-6-1.png)

    p1 + 
      geom_text(aes(label=State), size = 3)

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-7-1.png)

    ## install.packages("ggrepel") 
    library("ggrepel")
    p1 + 
      geom_point() + 
      geom_text_repel(aes(label=State), size = 3)

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-8-1.png)

    p1 +
      geom_point(aes(size = 2),# incorrect! 2 is not a variable
                 color="red") # this is fine -- all points red

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-9-1.png)

    p1 +
      geom_point(aes(color=Home.Value, shape = region))

    ## Warning: Removed 1 rows containing missing values (geom_point).

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-10-1.png)

Exercise 1
==========

    dat <- read.csv("/home/eeb177-student/Desktop/eeb-177/lab-work/exercise-8/Rgraphics/dataSets/EconomistData.csv")
    head(dat)

    ##   X     Country HDI.Rank   HDI CPI            Region
    ## 1 1 Afghanistan      172 0.398 1.5      Asia Pacific
    ## 2 2     Albania       70 0.739 3.1 East EU Cemt Asia
    ## 3 3     Algeria       96 0.698 2.9              MENA
    ## 4 4      Angola      148 0.486 2.0               SSA
    ## 5 5   Argentina       45 0.797 3.0          Americas
    ## 6 6     Armenia       86 0.716 2.6 East EU Cemt Asia

    ggplot(dat, aes(x = CPI, y = HDI, size = HDI.Rank)) + geom_point(aes(color = Region, size = HDI.Rank))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-11-1.png)

Statistical Transformations
===========================

    p2 <- ggplot(housing, aes(x = Home.Value))
    p2 + geom_histogram()

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-12-1.png)

    p2 + geom_histogram(stat = "bin", binwidth=4000)

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-13-1.png)

    housing.sum <- aggregate(housing["Home.Value"], housing["State"], FUN=mean)
    rbind(head(housing.sum), tail(housing.sum))

    ##    State Home.Value
    ## 1     AK  147385.14
    ## 2     AL   92545.22
    ## 3     AR   82076.84
    ## 4     AZ  140755.59
    ## 5     CA  282808.08
    ## 6     CO  158175.99
    ## 46    VA  155391.44
    ## 47    VT  132394.60
    ## 48    WA  178522.58
    ## 49    WI  108359.45
    ## 50    WV   77161.71
    ## 51    WY  122897.25

    ggplot(housing.sum, aes(x=State, y=Home.Value)) + 
      geom_bar(stat="identity")

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-15-1.png)
\# Exercise 2

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point() + geom_smooth(method = lm) + geom_line()

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-16-1.png)

Scales
======

    p3 <- ggplot(housing,
                 aes(x = State,
                     y = Home.Price.Index)) + 
            theme(legend.position="top",
                  axis.text=element_text(size = 6))
    (p4 <- p3 + geom_point(aes(color = Date),
                           alpha = 0.5,
                           size = 1.5,
                           position = position_jitter(width = 0.25, height = 0)))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-17-1.png)

    p4 + scale_x_discrete(name="State Abbreviation") +
      scale_color_continuous(name="",
                             breaks = c(1976, 1994, 2013),
                             labels = c("'76", "'94", "'13"))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-18-1.png)

    p4 +
      scale_x_discrete(name="State Abbreviation") +
      scale_color_continuous(name="",
                             breaks = c(1976, 1994, 2013),
                             labels = c("'76", "'94", "'13"),
                             low = "blue", high = "red")

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-19-1.png)

    p4 +
      scale_color_gradient2(name="",
                            breaks = c(1976, 1994, 2013),
                            labels = c("'76", "'94", "'13"),
                            low = ("blue"),
                            high = ("red"),
                            mid = "gray60",
                            midpoint = 1994)

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-20-1.png)
\# Exercise 3

    ggplot(dat, aes(x = CPI, y = HDI)) + geom_point(aes(color = Region))+ scale_x_discrete(name="Corruption Perceptions Index")+ scale_y_discrete(name="Human Development Index")+ scale_color_discrete(name="World Regions")+scale_color_manual(values = c("red","green","yellow","blue","orange","purple"))

    ## Scale for 'colour' is already present. Adding another scale for
    ## 'colour', which will replace the existing scale.

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-21-1.png)
\# Faceting

    p5 <- ggplot(housing, aes(x = Date, y = Home.Value))
    p5 + geom_line(aes(color = State))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-22-1.png)

    (p5 <- p5 + geom_line() +
       facet_wrap(~State, ncol = 10))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-23-1.png)
\# Themes

    p5 + theme_linedraw()

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-24-1.png)

    p5 + theme_minimal() +
      theme(text = element_text(color = "turquoise"))

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-25-1.png)

    theme_new <- theme_bw() +
      theme(plot.background = element_rect(size = 1, color = "blue", fill = "black"),
            text=element_text(size = 12, family = "Serif", color = "ivory"),
            axis.text.y = element_text(colour = "purple"),
            axis.text.x = element_text(colour = "red"),
            panel.background = element_rect(fill = "pink"),
            strip.background = element_rect(fill = ("orange")))

    p5 + theme_new

![](exercise-8_homework_files/figure-markdown_strict/unnamed-chunk-26-1.png)
