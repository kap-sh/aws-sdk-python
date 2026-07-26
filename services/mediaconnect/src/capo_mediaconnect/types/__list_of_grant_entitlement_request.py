"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfGrantEntitlementRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.grant_entitlement_request

__listOfGrantEntitlementRequest: TypeAlias = list[
    "capo_mediaconnect.types.grant_entitlement_request.GrantEntitlementRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGrantEntitlementRequest) -> list:
    import capo_mediaconnect.types.grant_entitlement_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.grant_entitlement_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfGrantEntitlementRequest:
    import capo_mediaconnect.types.grant_entitlement_request

    out: __listOfGrantEntitlementRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.grant_entitlement_request.deserialize_json(item)
        )
    return out
