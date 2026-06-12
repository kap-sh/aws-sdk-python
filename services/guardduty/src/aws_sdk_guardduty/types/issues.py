"""Generated from Smithy shape ``com.amazonaws.guardduty#Issues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

Issues: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Issues) -> list:
    return list(value)


def deserialize_json(data: list) -> Issues:
    return list(data)
