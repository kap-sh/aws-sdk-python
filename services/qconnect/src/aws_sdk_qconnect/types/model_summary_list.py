"""Generated from Smithy shape ``com.amazonaws.qconnect#ModelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.model_summary

ModelSummaryList: TypeAlias = list["aws_sdk_qconnect.types.model_summary.ModelSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelSummaryList) -> list:
    import aws_sdk_qconnect.types.model_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ModelSummaryList:
    import aws_sdk_qconnect.types.model_summary

    out: ModelSummaryList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.model_summary.deserialize_json(item))
    return out
