"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServerConnectorAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.connector_arn
    import aws_sdk_mgn.types.secret_arn


class SourceServerConnectorAction(TypedDict):
    credentials_secret_arn: NotRequired["aws_sdk_mgn.types.secret_arn.SecretArn"]
    """<p>Source Server connector action credentials secret arn.</p>"""
    connector_arn: NotRequired["aws_sdk_mgn.types.connector_arn.ConnectorArn"]
    """<p>Source Server connector action connector arn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerConnectorAction) -> dict:
    out: dict = {}
    if "credentials_secret_arn" in value:
        out["credentialsSecretArn"] = value["credentials_secret_arn"]
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> SourceServerConnectorAction:
    out: SourceServerConnectorAction = {}  # type: ignore[typeddict-item]
    if "credentialsSecretArn" in data:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    return out
