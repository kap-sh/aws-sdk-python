"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LinkAttributeUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.link_attribute_update

LinkAttributeUpdateList: TypeAlias = list[
    "aws_sdk_clouddirectory.types.link_attribute_update.LinkAttributeUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkAttributeUpdateList) -> list:
    import aws_sdk_clouddirectory.types.link_attribute_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_clouddirectory.types.link_attribute_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LinkAttributeUpdateList:
    import aws_sdk_clouddirectory.types.link_attribute_update

    out: LinkAttributeUpdateList = []
    for item in data:
        out.append(
            aws_sdk_clouddirectory.types.link_attribute_update.deserialize_json(item)
        )
    return out
