import click

@click.command()
@click.argument("username", type=str)
def hello(username):
    click.echo(f"Hello, {username}!")

if __name__ == '__main__':
    hello()
