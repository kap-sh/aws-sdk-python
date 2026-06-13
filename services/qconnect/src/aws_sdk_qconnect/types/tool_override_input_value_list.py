"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOverrideInputValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.tool_override_input_value

ToolOverrideInputValueList: TypeAlias = list[
    "aws_sdk_qconnect.types.tool_override_input_value.ToolOverrideInputValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolOverrideInputValueList) -> list:
    import aws_sdk_qconnect.types.tool_override_input_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.tool_override_input_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolOverrideInputValueList:
    import aws_sdk_qconnect.types.tool_override_input_value

    out: ToolOverrideInputValueList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.tool_override_input_value.deserialize_json(item)
        )
    return out
