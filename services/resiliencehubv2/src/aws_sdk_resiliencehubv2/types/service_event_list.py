"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_event

ServiceEventList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.service_event.ServiceEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEventList) -> list:
    import aws_sdk_resiliencehubv2.types.service_event

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.service_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEventList:
    import aws_sdk_resiliencehubv2.types.service_event

    out: ServiceEventList = []
    for item in data:
        out.append(aws_sdk_resiliencehubv2.types.service_event.deserialize_json(item))
    return out
