"""Generated from Smithy shape ``com.amazonaws.guardduty#Equals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

Equals: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Equals) -> list:
    return list(value)


def deserialize_json(data: list) -> Equals:
    return list(data)
