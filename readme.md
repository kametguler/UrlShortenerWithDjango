# Url Shortener Project

This is basic url shortener project which using sqlite.

* Django
* Django Rest Framework
* Sqlite

# API Reference

* Get all urls

  GET /all

[Response:]({
    "id": 3,
    "url": "https://github.com/gurkanucar",
    "code": "G"
})

`
[
{
"id": 1,
"url": "https://github.com/kametguler",
"code": "GIT"
},
{
"id": 2,
"url": "https://www.youtube.com/channel/UCkvuBt6THRFJqY_0TsTUdKw",
"code": "YT"
}
]`

* Redirect

  GET /{<str:code>}

You will be redirected to the URL of the code.

* Show Url of Code (alias)

  GET /show/{code}

* Create Short Url

  POST /

  [Request:]({
    "id": 3,
    "url": "https://github.com/gurkanucar",
    "code": "G"
})

  `{
    "url": "https://github.com/gurkanucar",
    "code": "g"
  }`

  [Response:]({
    "id": 3,
    "url": "https://github.com/gurkanucar",
    "code": "G"
}) 
  
  `{
    "id": 3,
    "url": "https://github.com/kametguler",
    "code": "G"
  }`

| Parameter | Type   | Description                                                         |
|-----------|--------|---------------------------------------------------------------------|
| url       | string | Required. Code of url to fetch                                      |
| code      | string | Not Required. If it is null or empty, it will be created automatically. |