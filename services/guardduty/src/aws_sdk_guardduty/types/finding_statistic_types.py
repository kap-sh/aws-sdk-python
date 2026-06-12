"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingStatisticTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding_statistic_type

FindingStatisticTypes: TypeAlias = list[
    "aws_sdk_guardduty.types.finding_statistic_type.FindingStatisticType"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatisticTypes) -> list:
    import aws_sdk_guardduty.types.finding_statistic_type

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.finding_statistic_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingStatisticTypes:
    import aws_sdk_guardduty.types.finding_statistic_type

    out: FindingStatisticTypes = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.finding_statistic_type.deserialize_json(item)
        )
    return out
