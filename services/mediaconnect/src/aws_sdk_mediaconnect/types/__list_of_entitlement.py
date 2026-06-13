"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfEntitlement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.entitlement

__listOfEntitlement: TypeAlias = list[
    "aws_sdk_mediaconnect.types.entitlement.Entitlement"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEntitlement) -> list:
    import aws_sdk_mediaconnect.types.entitlement

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.entitlement.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfEntitlement:
    import aws_sdk_mediaconnect.types.entitlement

    out: __listOfEntitlement = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.entitlement.deserialize_json(item))
    return out
