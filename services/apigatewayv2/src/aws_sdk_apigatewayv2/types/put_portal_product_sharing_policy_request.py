"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PutPortalProductSharingPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.__string_min1_max307200


class PutPortalProductSharingPolicyRequest(TypedDict):
    policy_document: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max307200.__stringMin1Max307200"
    ]
    """<p>The product sharing policy.</p>"""
    portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The portal product identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPortalProductSharingPolicyRequest) -> dict:
    out: dict = {}
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> PutPortalProductSharingPolicyRequest:
    out: PutPortalProductSharingPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    return out
