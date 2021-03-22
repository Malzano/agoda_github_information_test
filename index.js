const express = require('express')
const app = express()
const bodyParser = require("body-parser");
const { Octokit } = require("@octokit/core");
app.use(bodyParser.json());

//My own auth token
const octokit = new Octokit({ auth: '1598e3a3120b6e76de5a303a54813e06b3e0a977' })

app.get('/pulls/:owner/:repo', async function (req, res) {
    const resp =  await octokit.request('GET /repos/{owner}/{repo}/pulls', {
        owner: req.params.owner,
        repo: req.params.repo
      });
    res.json(resp.data);
});

app.get('/issues/:owner/:repo', async function (req, res) {
    const resp =  await octokit.request('GET /repos/{owner}/{repo}/issues', {
        owner: req.params.owner,
        repo: req.params.repo
      });
    res.json(resp.data);
});


 app.listen(process.env.PORT || 3000, () => console.log("listening on port 3000"))