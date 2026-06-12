"""Generated from Smithy shape ``com.amazonaws.guardduty#Groups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

Groups: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Groups) -> list:
    return list(value)


def deserialize_json(data: list) -> Groups:
    return list(data)
