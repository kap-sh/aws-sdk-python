"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_event

ServiceEvents: TypeAlias = list["aws_sdk_ecs.types.service_event.ServiceEvent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceEvents) -> list:
    import aws_sdk_ecs.types.service_event

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.service_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceEvents:
    import aws_sdk_ecs.types.service_event

    out: ServiceEvents = []
    for item in data:
        out.append(aws_sdk_ecs.types.service_event.deserialize_aws_json_1_1(item))
    return out
