"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_summary

ExperimentSummaryList: TypeAlias = list[
    "aws_sdk_fis.types.experiment_summary.ExperimentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentSummaryList) -> list:
    import aws_sdk_fis.types.experiment_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_fis.types.experiment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentSummaryList:
    import aws_sdk_fis.types.experiment_summary

    out: ExperimentSummaryList = []
    for item in data:
        out.append(aws_sdk_fis.types.experiment_summary.deserialize_json(item))
    return out
