"""Generated from Smithy shape ``com.amazonaws.devicefarm#AmazonResourceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name

AmazonResourceNames: TypeAlias = list[
    "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonResourceNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AmazonResourceNames:
    return list(data)
