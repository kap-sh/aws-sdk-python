"""Generated from Smithy shape ``com.amazonaws.lightsail#Environment``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string

Environment: TypeAlias = dict[
    "aws_sdk_lightsail.types.string.string", "aws_sdk_lightsail.types.string.string"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Environment) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Environment:
    out: Environment = {}
    for key, value in data.items():
        out[key] = value
    return out
