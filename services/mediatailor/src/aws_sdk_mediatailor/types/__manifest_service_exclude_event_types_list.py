"""Generated from Smithy shape ``com.amazonaws.mediatailor#__manifestServiceExcludeEventTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.manifest_service_exclude_event_type

__manifestServiceExcludeEventTypesList: TypeAlias = list[
    "aws_sdk_mediatailor.types.manifest_service_exclude_event_type.ManifestServiceExcludeEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __manifestServiceExcludeEventTypesList) -> list:
    import aws_sdk_mediatailor.types.manifest_service_exclude_event_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediatailor.types.manifest_service_exclude_event_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __manifestServiceExcludeEventTypesList:
    import aws_sdk_mediatailor.types.manifest_service_exclude_event_type

    out: __manifestServiceExcludeEventTypesList = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.manifest_service_exclude_event_type.deserialize_json(
                item
            )
        )
    return out
