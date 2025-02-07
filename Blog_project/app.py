from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for blog posts (for simplicity)
posts = []

# Home route - displays all blog posts
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Route to view a single post
@app.route('/post/<int:post_id>')
def post(post_id):
    if post_id < len(posts):
        post = posts[post_id]
        return render_template('post.html', post=post, post_id=post_id)
    return "Post not found", 404

# Route to create a new post
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('create.html')

# Route to edit an existing post
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    if post_id < len(posts):
        post = posts[post_id]
        if request.method == 'POST':
            post['title'] = request.form['title']
            post['content'] = request.form['content']
            return redirect(url_for('index'))
        return render_template('edit.html', post=post, post_id=post_id)
    return "Post not found", 404

# Route to delete a post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    if post_id < len(posts):
        posts.pop(post_id)
        return redirect(url_for('index'))
    return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True)