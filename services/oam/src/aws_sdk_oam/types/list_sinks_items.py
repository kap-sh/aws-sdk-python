"""Generated from Smithy shape ``com.amazonaws.oam#ListSinksItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_oam.types.list_sinks_item

ListSinksItems: TypeAlias = list["aws_sdk_oam.types.list_sinks_item.ListSinksItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ListSinksItems) -> list:
    import aws_sdk_oam.types.list_sinks_item

    out: list = []
    for item in value:
        out.append(aws_sdk_oam.types.list_sinks_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSinksItems:
    import aws_sdk_oam.types.list_sinks_item

    out: ListSinksItems = []
    for item in data:
        out.append(aws_sdk_oam.types.list_sinks_item.deserialize_json(item))
    return out
