"""Generated from Smithy shape ``com.amazonaws.qconnect#DataSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.data_summary

DataSummaryList: TypeAlias = list["aws_sdk_qconnect.types.data_summary.DataSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSummaryList) -> list:
    import aws_sdk_qconnect.types.data_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.data_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSummaryList:
    import aws_sdk_qconnect.types.data_summary

    out: DataSummaryList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.data_summary.deserialize_json(item))
    return out
