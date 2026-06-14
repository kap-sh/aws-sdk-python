"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime


class ConnectionCredentials(TypedDict):
    access_key_id: NotRequired["str"]
    """<p>The access key ID of a connection.</p>"""
    secret_access_key: NotRequired["str"]
    """<p>The secret access key of a connection.</p>"""
    session_token: NotRequired["str"]
    """<p>The session token of a connection credentials.</p>"""
    expiration: NotRequired["datetime.datetime"]
    """<p>The expiration of the connection credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionCredentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["secretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["sessionToken"] = value["session_token"]
    if "expiration" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["expiration"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["expiration"]
        )
    return out


def deserialize_json(data: dict) -> ConnectionCredentials:
    out: ConnectionCredentials = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    if "expiration" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["expiration"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["expiration"]
        )
    return out
