"""Generated from Smithy shape ``com.amazonaws.appsync#CognitoConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class CognitoConfig(TypedDict):
    user_pool_id: "aws_sdk_appsync.types.string.String"
    """<p>The user pool ID.</p>"""
    aws_region: "aws_sdk_appsync.types.string.String"
    """<p>The Amazon Web Services Region in which the user pool was created.</p>"""
    app_id_client_regex: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoConfig) -> dict:
    out: dict = {}
    out["userPoolId"] = value["user_pool_id"]
    out["awsRegion"] = value["aws_region"]
    if "app_id_client_regex" in value:
        out["appIdClientRegex"] = value["app_id_client_regex"]
    return out


def deserialize_json(data: dict) -> CognitoConfig:
    out: CognitoConfig = {}  # type: ignore[typeddict-item]
    if "userPoolId" in data:
        out["user_pool_id"] = data["userPoolId"]
    else:
        raise DeserializationError("CognitoConfig.user_pool_id required")
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    else:
        raise DeserializationError("CognitoConfig.aws_region required")
    if "appIdClientRegex" in data:
        out["app_id_client_regex"] = data["appIdClientRegex"]
    return out
