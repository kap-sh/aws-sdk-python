"""Generated from Smithy shape ``com.amazonaws.xray#TraceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.trace_summary

TraceSummaryList: TypeAlias = list["aws_sdk_xray.types.trace_summary.TraceSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceSummaryList) -> list:
    import aws_sdk_xray.types.trace_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.trace_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceSummaryList:
    import aws_sdk_xray.types.trace_summary

    out: TraceSummaryList = []
    for item in data:
        out.append(aws_sdk_xray.types.trace_summary.deserialize_json(item))
    return out
