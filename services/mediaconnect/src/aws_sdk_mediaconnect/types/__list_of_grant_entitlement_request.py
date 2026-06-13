"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfGrantEntitlementRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.grant_entitlement_request

__listOfGrantEntitlementRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.grant_entitlement_request.GrantEntitlementRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfGrantEntitlementRequest) -> list:
    import aws_sdk_mediaconnect.types.grant_entitlement_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.grant_entitlement_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfGrantEntitlementRequest:
    import aws_sdk_mediaconnect.types.grant_entitlement_request

    out: __listOfGrantEntitlementRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.grant_entitlement_request.deserialize_json(item)
        )
    return out
