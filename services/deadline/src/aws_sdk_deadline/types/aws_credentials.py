"""Generated from Smithy shape ``com.amazonaws.deadline#AwsCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.access_key_id
    import aws_sdk_deadline.types.secret_access_key
    import aws_sdk_deadline.types.session_token
    import aws_sdk_deadline.types.timestamp


class AwsCredentials(TypedDict, closed=True):
    access_key_id: "aws_sdk_deadline.types.access_key_id.AccessKeyId"
    """<p>The IAM access key ID.</p>"""
    secret_access_key: "aws_sdk_deadline.types.secret_access_key.SecretAccessKey"
    """<p>The IAM secret access key.</p>"""
    session_token: "aws_sdk_deadline.types.session_token.SessionToken"
    """<p>The IAM session token</p>"""
    expiration: "aws_sdk_deadline.types.timestamp.Timestamp"
    """<p>The expiration date and time of the IAM credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    import aws_sdk_deadline.types.timestamp

    out["expiration"] = aws_sdk_deadline.types.timestamp.serialize_json(
        value["expiration"]
    )
    return out


def deserialize_json(data: dict) -> AwsCredentials:
    out: AwsCredentials = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError("AwsCredentials.access_key_id required")
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        raise DeserializationError("AwsCredentials.secret_access_key required")
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    else:
        raise DeserializationError("AwsCredentials.session_token required")
    if "expiration" in data:
        import aws_sdk_deadline.types.timestamp

        out["expiration"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["expiration"]
        )
    else:
        raise DeserializationError("AwsCredentials.expiration required")
    return out
