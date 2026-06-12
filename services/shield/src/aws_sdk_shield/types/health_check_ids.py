"""Generated from Smithy shape ``com.amazonaws.shield#HealthCheckIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.health_check_id

HealthCheckIds: TypeAlias = list["aws_sdk_shield.types.health_check_id.HealthCheckId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthCheckIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HealthCheckIds:
    return list(data)
