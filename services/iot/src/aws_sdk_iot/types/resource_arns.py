"""Generated from Smithy shape ``com.amazonaws.iot#ResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.resource_arn
    import aws_sdk_iot.types.resource_logical_id

ResourceArns: TypeAlias = dict[
    "aws_sdk_iot.types.resource_logical_id.ResourceLogicalId",
    "aws_sdk_iot.types.resource_arn.ResourceArn",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceArns) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceArns:
    out: ResourceArns = {}
    for key, value in data.items():
        out[key] = value
    return out
