"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service_event_type

ServiceEventTypeList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.service_event_type.ServiceEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEventTypeList) -> list:
    import aws_sdk_resiliencehubv2.types.service_event_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.service_event_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceEventTypeList:
    import aws_sdk_resiliencehubv2.types.service_event_type

    out: ServiceEventTypeList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.service_event_type.deserialize_json(item)
        )
    return out
