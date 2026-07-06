"""Generated from Smithy shape ``com.amazonaws.finspacedata#AwsCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.access_key_id
    import aws_sdk_finspace_data.types.secret_access_key
    import aws_sdk_finspace_data.types.session_token
    import aws_sdk_finspace_data.types.timestamp_epoch


class AwsCredentials(TypedDict, closed=True):
    access_key_id: NotRequired["aws_sdk_finspace_data.types.access_key_id.AccessKeyId"]
    """<p> The unique identifier for the security credentials.</p>"""
    secret_access_key: NotRequired[
        "aws_sdk_finspace_data.types.secret_access_key.SecretAccessKey"
    ]
    """<p> The secret access key that can be used to sign requests.</p>"""
    session_token: NotRequired["aws_sdk_finspace_data.types.session_token.SessionToken"]
    """<p> The token that users must pass to use the credentials.</p>"""
    expiration: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p> The Epoch time when the current credentials expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCredentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["secretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["sessionToken"] = value["session_token"]
    out["expiration"] = value.get("expiration", 0)
    return out


def deserialize_json(data: dict) -> AwsCredentials:
    out: AwsCredentials = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    if "expiration" in data:
        out["expiration"] = data["expiration"]
    else:
        out["expiration"] = 0
    return out
