"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding_type

FindingTypes: TypeAlias = list["aws_sdk_guardduty.types.finding_type.FindingType"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingTypes:
    return list(data)
