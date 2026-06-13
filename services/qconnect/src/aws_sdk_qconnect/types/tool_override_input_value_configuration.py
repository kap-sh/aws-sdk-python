"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolOverrideInputValueConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.tool_override_constant_input_value


class _ToolOverrideInputValueConfiguration_constant(TypedDict):
    constant: "aws_sdk_qconnect.types.tool_override_constant_input_value.ToolOverrideConstantInputValue"


ToolOverrideInputValueConfiguration: TypeAlias = (
    _ToolOverrideInputValueConfiguration_constant
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolOverrideInputValueConfiguration) -> dict:
    if "constant" in value:
        import aws_sdk_qconnect.types.tool_override_constant_input_value

        return {
            "constant": aws_sdk_qconnect.types.tool_override_constant_input_value.serialize_json(
                value["constant"]
            )
        }
    else:
        raise SerializationError(
            "ToolOverrideInputValueConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> ToolOverrideInputValueConfiguration:
    if "constant" in data:
        import aws_sdk_qconnect.types.tool_override_constant_input_value

        return {
            "constant": aws_sdk_qconnect.types.tool_override_constant_input_value.deserialize_json(
                data["constant"]
            )
        }
    else:
        raise DeserializationError(
            "ToolOverrideInputValueConfiguration: no recognized variant key"
        )
