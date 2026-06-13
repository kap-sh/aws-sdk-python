"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfListedEntitlement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_entitlement

__listOfListedEntitlement: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_entitlement.ListedEntitlement"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListedEntitlement) -> list:
    import aws_sdk_mediaconnect.types.listed_entitlement

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.listed_entitlement.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfListedEntitlement:
    import aws_sdk_mediaconnect.types.listed_entitlement

    out: __listOfListedEntitlement = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.listed_entitlement.deserialize_json(item))
    return out
