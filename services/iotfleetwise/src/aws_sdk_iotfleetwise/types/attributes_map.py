"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#attributesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.attribute_name
    import aws_sdk_iotfleetwise.types.attribute_value

attributesMap: TypeAlias = dict[
    "aws_sdk_iotfleetwise.types.attribute_name.attributeName",
    "aws_sdk_iotfleetwise.types.attribute_value.attributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: attributesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> attributesMap:
    out: attributesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
