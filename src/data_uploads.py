import pkg_resources
import click
from config.flask_config import APP

@click.group()
def web():
    """Group all commands here"""
    pass

@click.command()
def version():
    """Displays the current build version"""
    version = pkg_resources.require("data_uploads")[0].version
    click.echo(version)

@click.command()
@click.option('--port', type=int, default=5000, help="Port to run the application")
def start_server(port):
    import logging
    logging.basicConfig()
    logger = logging.getLogger("IAM")
    logger.setLevel(logging.DEBUG)
    logger.info(f"launching on server {port}")
    from waitress import serve
    serve(APP, listen='*:{0}'.format(port), connection_limit=1000, asyncore_use_poll=True)
    
web.add_command(version)
web.add_command(start_server)