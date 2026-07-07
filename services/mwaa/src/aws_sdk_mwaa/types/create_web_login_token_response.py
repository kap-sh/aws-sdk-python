"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateWebLoginTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.airflow_identity
    import aws_sdk_mwaa.types.hostname
    import aws_sdk_mwaa.types.iam_identity
    import aws_sdk_mwaa.types.token


class CreateWebLoginTokenResponse(TypedDict, closed=True):
    web_token: NotRequired["aws_sdk_mwaa.types.token.Token"]
    """<p>An Airflow web server login token.</p>"""
    web_server_hostname: NotRequired["aws_sdk_mwaa.types.hostname.Hostname"]
    """<p>The Airflow web server hostname for the environment.</p>"""
    iam_identity: NotRequired["aws_sdk_mwaa.types.iam_identity.IamIdentity"]
    """<p>The name of the IAM identity creating the web login token. This might be an IAM user, or an assumed or federated identity. For example, <code>assumed-role/Admin/your-name</code>.</p>"""
    airflow_identity: NotRequired["aws_sdk_mwaa.types.airflow_identity.AirflowIdentity"]
    """<p>The user name of the Apache Airflow identity creating the web login token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebLoginTokenResponse) -> dict:
    out: dict = {}
    if "web_token" in value:
        out["WebToken"] = value["web_token"]
    if "web_server_hostname" in value:
        out["WebServerHostname"] = value["web_server_hostname"]
    if "iam_identity" in value:
        out["IamIdentity"] = value["iam_identity"]
    if "airflow_identity" in value:
        out["AirflowIdentity"] = value["airflow_identity"]
    return out


def deserialize_json(data: dict) -> CreateWebLoginTokenResponse:
    out: CreateWebLoginTokenResponse = {}  # type: ignore[typeddict-item]
    if "WebToken" in data:
        out["web_token"] = data["WebToken"]
    if "WebServerHostname" in data:
        out["web_server_hostname"] = data["WebServerHostname"]
    if "IamIdentity" in data:
        out["iam_identity"] = data["IamIdentity"]
    if "AirflowIdentity" in data:
        out["airflow_identity"] = data["AirflowIdentity"]
    return out
