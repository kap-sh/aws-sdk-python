"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateCliTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mwaa.types.hostname
    import aws_sdk_mwaa.types.token

class CreateCliTokenResponse(TypedDict):
    cli_token: NotRequired["aws_sdk_mwaa.types.token.Token"]
    """<p>An Airflow CLI login token.</p>"""
    web_server_hostname: NotRequired["aws_sdk_mwaa.types.hostname.Hostname"]
    """<p>The Airflow web server hostname for the environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateCliTokenResponse) -> dict:
    out: dict = {}
    if "cli_token" in value:
        out["CliToken"] = value["cli_token"]
    if "web_server_hostname" in value:
        out["WebServerHostname"] = value["web_server_hostname"]
    return out


def deserialize_json(data: dict) -> CreateCliTokenResponse:
    out: CreateCliTokenResponse = {}  # type: ignore[typeddict-item]
    if "CliToken" in data:
        out["cli_token"] = data["CliToken"]
    if "WebServerHostname" in data:
        out["web_server_hostname"] = data["WebServerHostname"]
    return out