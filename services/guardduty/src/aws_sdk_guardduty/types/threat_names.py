"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

ThreatNames: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatNames) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreatNames:
    return list(data)
