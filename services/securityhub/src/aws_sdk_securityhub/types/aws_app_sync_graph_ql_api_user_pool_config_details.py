"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiUserPoolConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsAppSyncGraphQlApiUserPoolConfigDetails(TypedDict):
    app_id_client_regex: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A regular expression for validating the incoming Amazon Cognito user pools app client ID. If this value isn't set, no filtering is applied. </p>"""
    aws_region: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Web Services Region in which the user pool was created. </p>"""
    default_action: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pools authentication doesn't match the Amazon Cognito user pools configuration. </p>"""
    user_pool_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The user pool ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAppSyncGraphQlApiUserPoolConfigDetails) -> dict:
    out: dict = {}
    if "app_id_client_regex" in value:
        out["AppIdClientRegex"] = value["app_id_client_regex"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "default_action" in value:
        out["DefaultAction"] = value["default_action"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_json(data: dict) -> AwsAppSyncGraphQlApiUserPoolConfigDetails:
    out: AwsAppSyncGraphQlApiUserPoolConfigDetails = {}  # type: ignore[typeddict-item]
    if "AppIdClientRegex" in data:
        out["app_id_client_regex"] = data["AppIdClientRegex"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    if "DefaultAction" in data:
        out["default_action"] = data["DefaultAction"]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    return out
