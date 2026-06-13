"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOutputFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.tool_output_filter

ToolOutputFilterList: TypeAlias = list[
    "aws_sdk_qconnect.types.tool_output_filter.ToolOutputFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolOutputFilterList) -> list:
    import aws_sdk_qconnect.types.tool_output_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.tool_output_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ToolOutputFilterList:
    import aws_sdk_qconnect.types.tool_output_filter

    out: ToolOutputFilterList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.tool_output_filter.deserialize_json(item))
    return out
