"""Generated from Smithy shape ``com.amazonaws.devicefarm#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.non_empty_string

SubnetIds: TypeAlias = list["capo_device_farm.types.non_empty_string.NonEmptyString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIds:
    return list(data)
