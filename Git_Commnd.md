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


