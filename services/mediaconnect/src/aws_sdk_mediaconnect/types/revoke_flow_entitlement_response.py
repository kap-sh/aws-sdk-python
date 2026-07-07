"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RevokeFlowEntitlementResponse``."""

from typing_extensions import NotRequired, TypedDict


class RevokeFlowEntitlementResponse(TypedDict, closed=True):
    entitlement_arn: NotRequired["str"]
    """<p> The ARN of the entitlement that was revoked.</p>"""
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that the entitlement was revoked from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeFlowEntitlementResponse) -> dict:
    out: dict = {}
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    return out


def deserialize_json(data: dict) -> RevokeFlowEntitlementResponse:
    out: RevokeFlowEntitlementResponse = {}  # type: ignore[typeddict-item]
    if "entitlementArn" in data:
        out["entitlement_arn"] = data["entitlementArn"]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    return out
