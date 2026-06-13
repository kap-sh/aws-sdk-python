"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GrantFlowEntitlementsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_entitlement


class GrantFlowEntitlementsResponse(TypedDict):
    entitlements: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_entitlement.__listOfEntitlement"
    ]
    """<p> The entitlements that were just granted.</p>"""
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that these entitlements were granted to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantFlowEntitlementsResponse) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import aws_sdk_mediaconnect.types.__list_of_entitlement

        out["entitlements"] = (
            aws_sdk_mediaconnect.types.__list_of_entitlement.serialize_json(
                value["entitlements"]
            )
        )
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    return out


def deserialize_json(data: dict) -> GrantFlowEntitlementsResponse:
    out: GrantFlowEntitlementsResponse = {}  # type: ignore[typeddict-item]
    if "entitlements" in data:
        import aws_sdk_mediaconnect.types.__list_of_entitlement

        out["entitlements"] = (
            aws_sdk_mediaconnect.types.__list_of_entitlement.deserialize_json(
                data["entitlements"]
            )
        )
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    return out
