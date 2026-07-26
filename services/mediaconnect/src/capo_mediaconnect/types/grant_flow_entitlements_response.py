"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GrantFlowEntitlementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_entitlement


class GrantFlowEntitlementsResponse(TypedDict, closed=True):
    entitlements: NotRequired[
        "capo_mediaconnect.types.__list_of_entitlement.__listOfEntitlement"
    ]
    """<p> The entitlements that were just granted.</p>"""
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that these entitlements were granted to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantFlowEntitlementsResponse) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import capo_mediaconnect.types.__list_of_entitlement

        out["entitlements"] = (
            capo_mediaconnect.types.__list_of_entitlement.serialize_json(
                value["entitlements"]
            )
        )
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    return out


def deserialize_json(data: dict) -> GrantFlowEntitlementsResponse:
    out: GrantFlowEntitlementsResponse = {}  # type: ignore[typeddict-item]
    if "entitlements" in data:
        import capo_mediaconnect.types.__list_of_entitlement

        out["entitlements"] = (
            capo_mediaconnect.types.__list_of_entitlement.deserialize_json(
                data["entitlements"]
            )
        )
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    return out
