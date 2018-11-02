
**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach hh
as shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduu
ce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observee
d properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of
LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```
# `LyaRT;Grid`

In this Universe everything is neat, even stochasticity.

Lyman alpha Resonant Scatter is dominated by random processes.

Although there is chaos, there is also an order.

## WARNING : THIS IS BETA VERSION! BUGS EVERYWHERE, BE AWARE!

## Origins and motivation

Due to the Lyman alpha Radiative Transfer large complexity, the efforts of understanding it moved from pure analytic studies to the so-called radiative transfer Monte Carlo (RTMC) codes that simulate Lyman alpha photons in arbitrary gas geometries. These codes provide useful information about the fraction of photons that manage to escape and the resulting Lyman alpha line profiles. The RTMC approach has shown to reproduce the observed properties of LAEs.

`LyaRT;Grid` is a publicly available `python` package based on a RTMC (Orsi et al. 2012) able to predict large amounts of Lyman alpha line profiles and escape fractions with high accuracy. We designed this code hoping that it helps researches all over the wolrd to get a better understanding of the Universe.

`LyaRT;Grid` is **fast** and **simple**.

+ **Fast** : This code is able to predict Lyman alpha escape fractions and line profiles in an unprecedentedly low amount of time. In particular thousands of escape fractions and line profiles can be computed in less than a second of computational time.

+ **Simple** : This code is *One-Line-Running*. Everyone, from a good trained monkey, passing through undergrade studients, to researches with basic python knowlege should be able to use `LyaRT;Grid`.

Although `LyaRT;Grid` is completely open source and is available for everyone, please, if you are using this code ( for whatever reason ) we will be very glad to hear about you and how you are using it. it's just a curiosity and efficiency matter. Maybe we can help you to have a smoother experience with `LyaRT;Grid`. For any issue or suggestion, please, contact `sidgurung@cefca.es`. Thank you.

## Installation

The easiest way to get `LyaRT;Grid` in your machine is through `pip`:

`pip install LyaRT_Grid`

This should do the trick. However, you can also install `LyaRT_Grid` downloading this repository and running

`pip install .`

in it.

In order to finish installation and check that everything is working properly, please, opening a `python`/`ipython` terminal and execute:

```python
import LyaRT_Grid as Lya

Lya.Test_Installation( Make_Plots = True )
```

This function checks if the pip installation downloaded everything. Then, if the data files are not found it tries to download them. Please, note that you should have about 1GB of free memory in you machine in order to install `LyaRT_Grid`. Also note that as ~1GB of data has to be downloaded, it might take some time depending on your internet conection.

After Checking that you have got the data in your machine `LyaRT_Grid` will check that everyhting works smoothly. For this some escape fractions and line profiles will be computed. The status of the operation should appear in the screen. Everything should get a `Succsess!!`. The only exception is

`Running :  Bicone_X_Slab Analytic --> ERROR. HUMAN IS DEAD. MISMATCH!!`

Do not worry. The only reason why you are getting this error is because this algorithm is not implemented yet. Then the function will produce some plots. In case you want to run the tests without plotting just set `Make_Plots = False`  when calling the `Lya.Test_Installation`.

This should be all for the installation. If you find any trouble/bug duruing it, please, contact us at `sidgurung@cefca.es`. Thank you for your patience.

## Hands on the code.

( Assuming everything went smoothly in the installation... )

**Congratulations!!** You have just become one of the few chosen ones in the history of humankind to have the great pleasure of using `LyaRT_Grid`.

**The units**: This code uses velocites in km/s , column densities in cm^{-2} and wavelengths in meters.

First let's have a look to the dynamical range of the different parameters covered by `LyaRT;Grid`. For this we only need to do:

```python
import LyaRT_Grid as Lya

Lya.Print_the_grid_edges()
```


### Predicting thousands of Lyman alpha escape fractions.

Let's move to one of the most powerful products of `LyaRT;Grid`: predicting huge amounts of Lyman alpha escape fractions.

In theory only one line is needed to predict the escape fraction for a thin shell geometry with expasion velocity (V) of 200km/s, logarithmic of column density (logNH) of 19.5 and dust optical depth (ta) of 0.1 :

```python
f_esc_Arr = Lya.RT_f_esc( 'Thin_Shell' , [ 200 ] , [ 19.5 ] , [ 0.1 ] )
```

In this way `f_esc_Arr` is an Array of 1 dimension and length 1 that contains the predicted escape fraction for this configuration.

However, `LyaRT;Grid` implements several gas geometries and is optimized to obtain large amount of escape fractions with only one line of code, so lets expand this a little bit more. If we want to compute the escape fraction in a thin shell outflow with the configurations { V , logNH , ta } , { 200 , 19.5 , 0.1 }, { 300 , 20.0 , 0.01 } and { 400 , 20.5 , 0.001 } we could do

```python
Geometry = 'Thin Shell' # Other options: 'Galactic Wind' or 'Bicone_X_Slab'

V_Arr     = [  200 ,  300 , 400   ] # Expansion velocity array in km/s

logNH_Arr = [ 19.5 , 20.0 , 20.5  ] # Logarithmic of column densities array in cm**-2

ta_Arr    = [  0.1 , 0.01 , 0.001 ] # Dust optical depth Array

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

The variable `f_esc_Arr` is an Array of 1 dimension and length 3 that encloses the escape fractions for the configurations. In particular `f_esc_Arr[i]` is computed using `V_Arr[i]` ,  `logNH_Arr[i]` and `ta_Arr[i]`.

If the user wants to change the outflow gas geometry, they only have to do

```python
Geometry = 'Galactic Wind' # Other options: 'Thin Shell' or 'Bicone_X_Slab'

f_esc_Arr = Lya.RT_f_esc( Geometry , V_Arr , logNH_Arr , ta_Arr )
```

