"""Generated from Smithy shape ``com.amazonaws.guardduty#NotMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.not_match

NotMatches: TypeAlias = list["aws_sdk_guardduty.types.not_match.NotMatch"]


# --- restJson1 ser/de ---
def serialize_json(value: NotMatches) -> list:
    return list(value)


def deserialize_json(data: list) -> NotMatches:
    return list(data)
