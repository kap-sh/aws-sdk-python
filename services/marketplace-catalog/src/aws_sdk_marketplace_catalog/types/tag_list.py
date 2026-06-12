"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.tag

TagList: TypeAlias = list["aws_sdk_marketplace_catalog.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import aws_sdk_marketplace_catalog.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_catalog.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import aws_sdk_marketplace_catalog.types.tag

    out: TagList = []
    for item in data:
        out.append(aws_sdk_marketplace_catalog.types.tag.deserialize_json(item))
    return out
