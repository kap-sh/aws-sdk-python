"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceMetadataEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string

ContainerServiceMetadataEntry: TypeAlias = dict[
    "aws_sdk_lightsail.types.string.string", "aws_sdk_lightsail.types.string.string"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ContainerServiceMetadataEntry) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceMetadataEntry:
    out: ContainerServiceMetadataEntry = {}
    for key, value in data.items():
        out[key] = value
    return out
