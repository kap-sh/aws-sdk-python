"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingsStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.findings_statistics

FindingsStatisticsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.findings_statistics.FindingsStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsStatisticsList) -> list:
    import aws_sdk_accessanalyzer.types.findings_statistics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.findings_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsStatisticsList:
    import aws_sdk_accessanalyzer.types.findings_statistics

    out: FindingsStatisticsList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.findings_statistics.deserialize_json(item)
        )
    return out
