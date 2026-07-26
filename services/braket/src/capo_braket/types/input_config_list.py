"""Generated from Smithy shape ``com.amazonaws.braket#InputConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.input_file_config

InputConfigList: TypeAlias = list["capo_braket.types.input_file_config.InputFileConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: InputConfigList) -> list:
    import capo_braket.types.input_file_config

    out: list = []
    for item in value:
        out.append(capo_braket.types.input_file_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputConfigList:
    import capo_braket.types.input_file_config

    out: InputConfigList = []
    for item in data:
        out.append(capo_braket.types.input_file_config.deserialize_json(item))
    return out
