"""Generated from Smithy shape ``com.amazonaws.appsync#UserPoolConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.default_action
    import capo_appsync.types.string


class UserPoolConfig(TypedDict, closed=True):
    user_pool_id: "capo_appsync.types.string.String"
    """<p>The user pool ID.</p>"""
    aws_region: "capo_appsync.types.string.String"
    """<p>The Amazon Web Services Region in which the user pool was created.</p>"""
    default_action: "capo_appsync.types.default_action.DefaultAction"
    """<p>The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.</p>"""
    app_id_client_regex: NotRequired["capo_appsync.types.string.String"]
    """<p>A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPoolConfig) -> dict:
    out: dict = {}
    out["userPoolId"] = value["user_pool_id"]
    out["awsRegion"] = value["aws_region"]
    import capo_appsync.types.default_action

    out["defaultAction"] = capo_appsync.types.default_action.serialize_json(
        value["default_action"]
    )
    if "app_id_client_regex" in value:
        out["appIdClientRegex"] = value["app_id_client_regex"]
    return out


def deserialize_json(data: dict) -> UserPoolConfig:
    out: UserPoolConfig = {}  # type: ignore[typeddict-item]
    if "userPoolId" in data:
        out["user_pool_id"] = data["userPoolId"]
    else:
        raise DeserializationError("UserPoolConfig.user_pool_id required")
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    else:
        raise DeserializationError("UserPoolConfig.aws_region required")
    if "defaultAction" in data:
        import capo_appsync.types.default_action

        out["default_action"] = capo_appsync.types.default_action.deserialize_json(
            data["defaultAction"]
        )
    else:
        raise DeserializationError("UserPoolConfig.default_action required")
    if "appIdClientRegex" in data:
        out["app_id_client_regex"] = data["appIdClientRegex"]
    return out
