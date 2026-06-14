"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetPortalProductSharingPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max307200
    import aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09


class GetPortalProductSharingPolicyResponse(TypedDict):
    policy_document: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max307200.__stringMin1Max307200"
    ]
    """<p>The product sharing policy.</p>"""
    portal_product_id: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min10_max30_pattern_az09.__stringMin10Max30PatternAZ09"
    ]
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalProductSharingPolicyResponse) -> dict:
    out: dict = {}
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "portal_product_id" in value:
        out["portalProductId"] = value["portal_product_id"]
    return out


def deserialize_json(data: dict) -> GetPortalProductSharingPolicyResponse:
    out: GetPortalProductSharingPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "portalProductId" in data:
        out["portal_product_id"] = data["portalProductId"]
    return out
