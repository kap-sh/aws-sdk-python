"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceHealthStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.health_status
    import aws_sdk_servicediscovery.types.resource_id

InstanceHealthStatusMap: TypeAlias = dict[
    "aws_sdk_servicediscovery.types.resource_id.ResourceId",
    "aws_sdk_servicediscovery.types.health_status.HealthStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: InstanceHealthStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_servicediscovery.types.health_status

        out[key] = aws_sdk_servicediscovery.types.health_status.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceHealthStatusMap:
    out: InstanceHealthStatusMap = {}
    for key, value in data.items():
        import aws_sdk_servicediscovery.types.health_status

        out[key] = (
            aws_sdk_servicediscovery.types.health_status.deserialize_aws_json_1_1(value)
        )
    return out
