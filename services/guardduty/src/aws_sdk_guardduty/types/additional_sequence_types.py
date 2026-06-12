"""Generated from Smithy shape ``com.amazonaws.guardduty#AdditionalSequenceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding_type

AdditionalSequenceTypes: TypeAlias = list[
    "aws_sdk_guardduty.types.finding_type.FindingType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalSequenceTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalSequenceTypes:
    return list(data)
