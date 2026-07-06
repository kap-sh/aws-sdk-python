"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RevokeFlowEntitlementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn


class RevokeFlowEntitlementRequest(TypedDict, closed=True):
    entitlement_arn: "str"
    """<p> The Amazon Resource Name (ARN) of the entitlement that you want to revoke.</p>"""
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The flow that you want to revoke an entitlement from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeFlowEntitlementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RevokeFlowEntitlementRequest:
    out: RevokeFlowEntitlementRequest = {}  # type: ignore[typeddict-item]
    return out
