"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.integer

IntegerList: TypeAlias = list["capo_securityhub.types.integer.Integer"]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntegerList:
    return list(data)
