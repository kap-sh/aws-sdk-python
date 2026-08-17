"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_event

ServiceEvents: TypeAlias = list["capo_ecs.types.service_event.ServiceEvent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceEvents) -> list:
    import capo_ecs.types.service_event

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceEvents:
    import capo_ecs.types.service_event

    out: ServiceEvents = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.service_event.deserialize_aws_json_1_1(item))
    return out
