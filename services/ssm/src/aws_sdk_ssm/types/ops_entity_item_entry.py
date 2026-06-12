"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntityItemEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.attribute_name
    import aws_sdk_ssm.types.attribute_value

OpsEntityItemEntry: TypeAlias = dict[
    "aws_sdk_ssm.types.attribute_name.AttributeName",
    "aws_sdk_ssm.types.attribute_value.AttributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: OpsEntityItemEntry) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsEntityItemEntry:
    out: OpsEntityItemEntry = {}
    for key, value in data.items():
        out[key] = value
    return out
