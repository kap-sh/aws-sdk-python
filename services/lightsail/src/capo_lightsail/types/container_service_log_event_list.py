"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceLogEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_log_event

ContainerServiceLogEventList: TypeAlias = list[
    "capo_lightsail.types.container_service_log_event.ContainerServiceLogEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceLogEventList) -> list:
    import capo_lightsail.types.container_service_log_event

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.container_service_log_event.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerServiceLogEventList:
    import capo_lightsail.types.container_service_log_event

    out: ContainerServiceLogEventList = []
    for item in data:
        out.append(
            capo_lightsail.types.container_service_log_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out
