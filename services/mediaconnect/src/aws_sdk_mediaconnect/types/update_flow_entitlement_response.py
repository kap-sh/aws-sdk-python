"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowEntitlementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.entitlement


class UpdateFlowEntitlementResponse(TypedDict, closed=True):
    entitlement: NotRequired["aws_sdk_mediaconnect.types.entitlement.Entitlement"]
    """<p> The new configuration of the entitlement that you updated.</p>"""
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that this entitlement was granted on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowEntitlementResponse) -> dict:
    out: dict = {}
    if "entitlement" in value:
        import aws_sdk_mediaconnect.types.entitlement

        out["entitlement"] = aws_sdk_mediaconnect.types.entitlement.serialize_json(
            value["entitlement"]
        )
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    return out


def deserialize_json(data: dict) -> UpdateFlowEntitlementResponse:
    out: UpdateFlowEntitlementResponse = {}  # type: ignore[typeddict-item]
    if "entitlement" in data:
        import aws_sdk_mediaconnect.types.entitlement

        out["entitlement"] = aws_sdk_mediaconnect.types.entitlement.deserialize_json(
            data["entitlement"]
        )
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    return out
