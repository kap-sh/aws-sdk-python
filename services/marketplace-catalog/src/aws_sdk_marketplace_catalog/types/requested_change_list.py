"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#RequestedChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.change

RequestedChangeList: TypeAlias = list["aws_sdk_marketplace_catalog.types.change.Change"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestedChangeList) -> list:
    import aws_sdk_marketplace_catalog.types.change

    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_catalog.types.change.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequestedChangeList:
    import aws_sdk_marketplace_catalog.types.change

    out: RequestedChangeList = []
    for item in data:
        out.append(aws_sdk_marketplace_catalog.types.change.deserialize_json(item))
    return out
