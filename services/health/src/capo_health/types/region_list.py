"""Generated from Smithy shape ``com.amazonaws.health#regionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.region

regionList: TypeAlias = list["capo_health.types.region.region"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: regionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> regionList:
    return list(data)
