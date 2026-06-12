"""Generated from Smithy shape ``com.amazonaws.codepipeline#AWSSessionCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.access_key_id
    import aws_sdk_codepipeline.types.secret_access_key
    import aws_sdk_codepipeline.types.session_token


class AWSSessionCredentials(TypedDict):
    access_key_id: "aws_sdk_codepipeline.types.access_key_id.AccessKeyId"
    """<p>The access key for the session.</p>"""
    secret_access_key: "aws_sdk_codepipeline.types.secret_access_key.SecretAccessKey"
    """<p>The secret access key for the session.</p>"""
    session_token: "aws_sdk_codepipeline.types.session_token.SessionToken"
    """<p>The token for the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSSessionCredentials) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSSessionCredentials:
    out: AWSSessionCredentials = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    else:
        raise DeserializationError("AWSSessionCredentials.access_key_id required")
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        raise DeserializationError("AWSSessionCredentials.secret_access_key required")
    if "sessionToken" in data:
        out["session_token"] = data["sessionToken"]
    else:
        raise DeserializationError("AWSSessionCredentials.session_token required")
    return out
