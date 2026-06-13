"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.input_source_summary

InputSourceSummaryList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.input_source_summary.InputSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceSummaryList) -> list:
    import aws_sdk_resiliencehubv2.types.input_source_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.input_source_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InputSourceSummaryList:
    import aws_sdk_resiliencehubv2.types.input_source_summary

    out: InputSourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.input_source_summary.deserialize_json(item)
        )
    return out
