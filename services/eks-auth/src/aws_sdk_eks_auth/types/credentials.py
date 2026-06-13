"""Generated from Smithy shape ``com.amazonaws.eksauth#Credentials``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eks_auth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class Credentials(TypedDict):
    session_token: "str"
    """<p>The token that applications inside the pods must pass to any service API to use the temporary credentials.</p>"""
    secret_access_key: "str"
    """<p>The secret access key that applications inside the pods use to sign requests.</p>"""
    access_key_id: "str"
    """<p>The access key ID that identifies the temporary security credentials.</p>"""
    expiration: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds when the current credentials expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    out: dict = {}
    out["sessionToken"] = value["session_token"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["accessKeyId"] = value["access_key_id"]
    import aws_sdk_eks_auth.types._prelude.timestamp

    out["expiration"] = aws_sdk_eks_auth.types._prelude.timestamp.serialize_json(
        value["expiration"]
    )
    return out


def deserialize_json(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    else:
        raise DeserializationError("Credentials.session_token required")
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        raise DeserializationError("Credentials.secret_access_key required")
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError("Credentials.access_key_id required")
    if "expiration" in data:
        import aws_sdk_eks_auth.types._prelude.timestamp

        out["expiration"] = aws_sdk_eks_auth.types._prelude.timestamp.deserialize_json(
            data["expiration"]
        )
    else:
        raise DeserializationError("Credentials.expiration required")
    return out
