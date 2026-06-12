"""Generated from Smithy shape ``com.amazonaws.guardduty#NotEquals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

NotEquals: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: NotEquals) -> list:
    return list(value)


def deserialize_json(data: list) -> NotEquals:
    return list(data)
