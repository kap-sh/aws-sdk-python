"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingsListV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_summary_v2

FindingsListV2: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.finding_summary_v2.FindingSummaryV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsListV2) -> list:
    import aws_sdk_accessanalyzer.types.finding_summary_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.finding_summary_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingsListV2:
    import aws_sdk_accessanalyzer.types.finding_summary_v2

    out: FindingsListV2 = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.finding_summary_v2.deserialize_json(item)
        )
    return out
