"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CognitoConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string_min1_max256
    import capo_apigatewayv2.types.__string_min20_max2048


class CognitoConfig(TypedDict, closed=True):
    app_client_id: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max256.__stringMin1Max256"
    ]
    """<p>The app client ID.</p>"""
    user_pool_arn: NotRequired[
        "capo_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The user pool ARN.</p>"""
    user_pool_domain: NotRequired[
        "capo_apigatewayv2.types.__string_min20_max2048.__stringMin20Max2048"
    ]
    """<p>The user pool domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoConfig) -> dict:
    out: dict = {}
    if "app_client_id" in value:
        out["appClientId"] = value["app_client_id"]
    if "user_pool_arn" in value:
        out["userPoolArn"] = value["user_pool_arn"]
    if "user_pool_domain" in value:
        out["userPoolDomain"] = value["user_pool_domain"]
    return out


def deserialize_json(data: dict) -> CognitoConfig:
    out: CognitoConfig = {}  # type: ignore[typeddict-item]
    if "appClientId" in data:
        out["app_client_id"] = data["appClientId"]
    if "userPoolArn" in data:
        out["user_pool_arn"] = data["userPoolArn"]
    if "userPoolDomain" in data:
        out["user_pool_domain"] = data["userPoolDomain"]
    return out
