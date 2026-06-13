"""Generated from Smithy shape ``com.amazonaws.braket#InputConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.input_file_config

InputConfigList: TypeAlias = list[
    "aws_sdk_braket.types.input_file_config.InputFileConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputConfigList) -> list:
    import aws_sdk_braket.types.input_file_config

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.input_file_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputConfigList:
    import aws_sdk_braket.types.input_file_config

    out: InputConfigList = []
    for item in data:
        out.append(aws_sdk_braket.types.input_file_config.deserialize_json(item))
    return out
