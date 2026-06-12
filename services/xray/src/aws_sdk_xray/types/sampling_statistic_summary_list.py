"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStatisticSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_statistic_summary

SamplingStatisticSummaryList: TypeAlias = list[
    "aws_sdk_xray.types.sampling_statistic_summary.SamplingStatisticSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStatisticSummaryList) -> list:
    import aws_sdk_xray.types.sampling_statistic_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.sampling_statistic_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SamplingStatisticSummaryList:
    import aws_sdk_xray.types.sampling_statistic_summary

    out: SamplingStatisticSummaryList = []
    for item in data:
        out.append(aws_sdk_xray.types.sampling_statistic_summary.deserialize_json(item))
    return out
