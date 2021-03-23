# Gitでできること
* **コミット**　リポジトリに変更履歴を記録する
* **ブランチ**変更履歴を分岐する
* **ログ**変更履歴を確認する
* **プッシュプル**変更履歴を共有する
* **ステージング**コミットの対象となるファイルとフォルダを選別する手順

## リポジトリとは
* Gitではプロジェクト単位で変更履歴を管理する
* プロジェクトごとの**変更履歴を記録するための場所をリポジトリ**という
# GitHubでのリモートリポジトリの作成
* GitHubにログイン、トップページの「Create repository」（New）をクリックする。

1. Repository name: リポジトリ名　（複数の単語をつなげるときはハイフォン「-」を使用する
1. Description: リポジトリの説明
1. Public/Private: 公開するかどうか
1. 「Create repository」　をクリックするとリモートリポジトリが作成される
1. URLをコピーしてメモしておく

# Gitでリモートリポジトリのクローンをする方法
* 上記でGitHub上にリモートリポジトリを作成済みなので、ローカル環境にそのコピーを作り、それをローカルリポジトリとする。
この操作を「クローン」という。
* GitHubにログインして、作成したリポジトリにアクセスし、「Quick setup」などとある欄に、URLとコピーをするアイコンがあるので、クリックしてコピーする。

## リポジトリをクローンする
1. Get Bashを開いて、**git cloneコマンドでクローン**をする「git clone *https://github.com/moyoshiyu/test.git*」
2. Git Bashでは「Ctrl」＋「v」による貼り付けができない。右クリックメニューから「Paste」をクリック
3. 「Connect to GitHub」という画面に「Sign in with your browser」をクリック
4. ブラウザで「Authorize Git Credential Manager」というページが開くので、緑の「Authorize GitCredentialManager」をクリック
5. GitHubのパスワードの入力し、「Confirm password」をクリック
6. 「Authentication Succeeded」つまり認証成功となり、つまりGitからGitHubへのアクセスが許可されたということになる

## クローされたローカルリポジトリを確認する
1. 作成されたディレクトリ「test」に移動する「cd test」
1. 「ls -a」フォルダ内に「.git」ローカルリポジトリがある

## Gitのコミットをして変更履歴を記録する方法
1. **git addコマンド**でステージングする
* git add *ファイルまたはフォルダ*
* カレントディレクトリすべて対象は**git add.**
2. **git status**コマンドでリポジトリの状態を確認する
* 「On branch *ブランチ名*」(master)現在のブランチ
* 「No commits yet」　コミットがないと表示
* 「Changes to be committed:」ステージングされていてコミットされていないファイルが緑色で表示される
~~~
yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Git_Commnd.md

nothing added to commit but untracked files present (use "git add" to track)

yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$ git add .

yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Git_Commnd.md

yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$
~~~

### git commitコマンドでコミットする
1. **git commit**実行すると、VS Codeが反応して「COMMIT_EDITMSG」というタブが開く
* 1行目にコミットのタイトル 
* 2行目は空けて、3行目以降に詳細を書いていく
* 書き終わったら `Ctrl`+`s`で保存
* 「COMMIT_EDITMSG」タブを「×」で閉じる
* コミットの結果を確認
* リポジトリの状態 **git status**
* コミットの履歴を確認 **git log**
* 

# リモートリポジトリに変更履歴を反映する方法
## リモートリポジトリに変更履歴を反映する**git push**コマンド
* git push *リモートリポジトリ名　ブランチ名*
## リモートリポジトリ名を調べる
* git remote
~~~
yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$ git remote
origin

yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$
~~~
* 「origin」がリモートリポジトリ名
## ブランチ名を調べる
* git status
~~~
yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$
~~~
* On branch **master** がブランチ名
## リモートリポジトリにプッシュする
* リモートリポジトリ名: origin
* ブランチ名: master
* 「`git push origin master`」
```
yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$ git push origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.48 KiB | 1.24 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/moyoshiyu/test.git
   f6bc2ea..5679b8b  master -> master

yoshiyuki@yoshiyuki1 MINGW64 ~/test (master)
$
```

  

----
# Gitコマンド
|コマンド |内容 |
|----|----|
|clear|画面クリア|
|git --version |バージョン確認|
|git config --global user.name ユーザー名|ユーザー登録|
|git config --global user.email メールアドレス|メールアドレス登録|
|git config --global core.editor "code --wait"|エディタをVS Codeに設定|
|git config --list|設定確認|
|git config *--core.editor*|特定の設定項目のみ確認|
|code .|VS Codeを立ち上げる|


