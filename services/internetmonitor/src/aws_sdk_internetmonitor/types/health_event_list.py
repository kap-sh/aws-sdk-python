"""Generated from Smithy shape ``com.amazonaws.internetmonitor#HealthEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.health_event

HealthEventList: TypeAlias = list[
    "aws_sdk_internetmonitor.types.health_event.HealthEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: HealthEventList) -> list:
    import aws_sdk_internetmonitor.types.health_event

    out: list = []
    for item in value:
        out.append(aws_sdk_internetmonitor.types.health_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> HealthEventList:
    import aws_sdk_internetmonitor.types.health_event

    out: HealthEventList = []
    for item in data:
        out.append(aws_sdk_internetmonitor.types.health_event.deserialize_json(item))
    return out
