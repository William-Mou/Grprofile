# todo_list

1. 收集資料 頁面
    * 前端 bootstrap
    * 後端 flask
2. 處理轉換成 csv 儲存
    * 每 row 分別為個資
    * mail 必須是第一 column
    * 接續 column 為 profiles
3. 傳送資料 API
    * 單人資料：md5(mail)
    * 多人資料：接收多人 md5(mail).csv，回傳多人 csv
4. server 架設：
    * GCP 架設資料庫
    * GCP 部署 container
