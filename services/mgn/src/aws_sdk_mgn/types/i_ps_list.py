"""Generated from Smithy shape ``com.amazonaws.mgn#IPsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string

IPsList: TypeAlias = list["aws_sdk_mgn.types.bounded_string.BoundedString"]


# --- restJson1 ser/de ---
def serialize_json(value: IPsList) -> list:
    return list(value)


def deserialize_json(data: list) -> IPsList:
    return list(data)