"""Generated from Smithy shape ``com.amazonaws.entityresolution#InputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.input_source

InputSourceConfig: TypeAlias = list[
    "aws_sdk_entityresolution.types.input_source.InputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceConfig) -> list:
    import aws_sdk_entityresolution.types.input_source

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.input_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> InputSourceConfig:
    import aws_sdk_entityresolution.types.input_source

    out: InputSourceConfig = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.input_source.deserialize_json(item))
    return out
