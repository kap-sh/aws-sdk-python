"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GrantFlowEntitlementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_grant_entitlement_request
    import capo_mediaconnect.types.flow_arn


class GrantFlowEntitlementsRequest(TypedDict, closed=True):
    entitlements: NotRequired[
        "capo_mediaconnect.types.__list_of_grant_entitlement_request.__listOfGrantEntitlementRequest"
    ]
    """<p> The list of entitlements that you want to grant.</p>"""
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to grant entitlements on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantFlowEntitlementsRequest) -> dict:
    out: dict = {}
    if "entitlements" in value:
        import capo_mediaconnect.types.__list_of_grant_entitlement_request

        out["entitlements"] = (
            capo_mediaconnect.types.__list_of_grant_entitlement_request.serialize_json(
                value["entitlements"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrantFlowEntitlementsRequest:
    out: GrantFlowEntitlementsRequest = {}  # type: ignore[typeddict-item]
    if "entitlements" in data:
        import capo_mediaconnect.types.__list_of_grant_entitlement_request

        out["entitlements"] = (
            capo_mediaconnect.types.__list_of_grant_entitlement_request.deserialize_json(
                data["entitlements"]
            )
        )
    return out
