"""Generated from Smithy shape ``com.amazonaws.outposts#OrderIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.string

OrderIdList: TypeAlias = list["aws_sdk_outposts.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: OrderIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrderIdList:
    return list(data)
