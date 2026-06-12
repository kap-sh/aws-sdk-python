"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatIntelSetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

ThreatIntelSetIds: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelSetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreatIntelSetIds:
    return list(data)
