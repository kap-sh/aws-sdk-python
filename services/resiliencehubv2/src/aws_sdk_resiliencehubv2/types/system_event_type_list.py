"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.system_event_type

SystemEventTypeList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.system_event_type.SystemEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventTypeList) -> list:
    import aws_sdk_resiliencehubv2.types.system_event_type

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.system_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SystemEventTypeList:
    import aws_sdk_resiliencehubv2.types.system_event_type

    out: SystemEventTypeList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.system_event_type.deserialize_json(item)
        )
    return out
