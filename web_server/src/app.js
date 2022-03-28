const path = require('path')
const express = require('express')
const hbs = require('hbs')

const {PythonShell} = require('python-shell')

const app = express()
const port = process.env.PORT || 3000

// Define paths for Express config
const publicDirectoryPath = path.join(__dirname, '../public')
const viewsPath = path.join(__dirname, '../templates/views')
const partialsPath = path.join(__dirname, '../templates/partials')
const pyscript = path.join(__dirname, '../ml/script.py')

// Setup handlebars engine and views location
app.set('view engine', 'hbs')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)

// Setup static directory to serve
app.use(express.static(publicDirectoryPath))

app.get('', (req, res) => {
    res.render('index', {
        title: 'CovidInfo',
        name: 'Smit Contractor'
    })
})

app.get('/insights', (req, res) => {
    res.render('insights', {
        title: 'Insights',
        name: 'Smit Contractor'
    })
})

app.get('/model_performance', (req, res) => {
    res.render('model_performance', {
        title: 'ModelPerformance',
        name: 'Smit Contractor'
    })
})

app.get('/prediction', (req, res) => {
    res.render('prediction', {
        title: 'Prediction',
        name: 'Smit Contractor'
    })
})

app.get('/about', (req, res) => {
    res.render('about', {
        title: 'About Me',
        name: 'Smit Contractor'
    })
})

app.get('/help', (req, res) => {
    res.render('help', {
        helpText: 'This is some helpful text.',
        title: 'Help',
        name: 'Smit Contractor'
    })
})

app.get('/get-prediction', (req, res) => {
    console.log(req.query)
    PythonShell.run(pyscript, null, async (err, results) => {
        if (err) {
            console.log(err)
            return res.send({
                error: 'Something went wrong'
            })
        }
        console.log(results)
        return res.send({
            result: results
        })
      });
})

app.get('/help/*', (req, res) => {
    res.render('404', {
        title: '404',
        name: 'Smit Contractor',
        errorMessage: 'Help article not found.'
    })
})

app.get('*', (req, res) => {
    res.render('404', {
        title: '404',
        name: 'Smit Contractor',
        errorMessage: 'Page not found.'
    })
})

app.listen(port, () => {
    console.log('Server is up on port ' + port)
})