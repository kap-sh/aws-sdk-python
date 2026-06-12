"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.access_key_id
    import aws_sdk_appflow.types.key
    import aws_sdk_appflow.types.username


class InforNexusConnectorProfileCredentials(TypedDict):
    access_key_id: "aws_sdk_appflow.types.access_key_id.AccessKeyId"
    """<p> The Access Key portion of the credentials. </p>"""
    user_id: "aws_sdk_appflow.types.username.Username"
    """<p> The identifier for the user. </p>"""
    secret_access_key: "aws_sdk_appflow.types.key.Key"
    """<p> The secret key used to sign requests. </p>"""
    datakey: "aws_sdk_appflow.types.key.Key"
    """<p> The encryption keys used to encrypt data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InforNexusConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["userId"] = value["user_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["datakey"] = value["datakey"]
    return out


def deserialize_json(data: dict) -> InforNexusConnectorProfileCredentials:
    out: InforNexusConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError(
            "InforNexusConnectorProfileCredentials.access_key_id required"
        )
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError(
            "InforNexusConnectorProfileCredentials.user_id required"
        )
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        raise DeserializationError(
            "InforNexusConnectorProfileCredentials.secret_access_key required"
        )
    if "datakey" in data:
        out["datakey"] = data["datakey"]
    else:
        raise DeserializationError(
            "InforNexusConnectorProfileCredentials.datakey required"
        )
    return out
