"""Generated from Smithy shape ``com.amazonaws.health#serviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.service

serviceList: TypeAlias = list["capo_health.types.service.service"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: serviceList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> serviceList:
    return list(data)
