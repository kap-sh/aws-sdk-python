"""Generated from Smithy shape ``com.amazonaws.entityresolution#OutputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.output_source

OutputSourceConfig: TypeAlias = list[
    "aws_sdk_entityresolution.types.output_source.OutputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputSourceConfig) -> list:
    import aws_sdk_entityresolution.types.output_source

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.output_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputSourceConfig:
    import aws_sdk_entityresolution.types.output_source

    out: OutputSourceConfig = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.output_source.deserialize_json(item))
    return out
