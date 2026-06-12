"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_instance_filter_value

SystemInstanceFilterValues: TypeAlias = list[
    "aws_sdk_iotthingsgraph.types.system_instance_filter_value.SystemInstanceFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SystemInstanceFilterValues:
    return list(data)
