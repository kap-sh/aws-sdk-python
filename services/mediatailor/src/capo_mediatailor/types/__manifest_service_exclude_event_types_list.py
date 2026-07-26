"""Generated from Smithy shape ``com.amazonaws.mediatailor#__manifestServiceExcludeEventTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.manifest_service_exclude_event_type

__manifestServiceExcludeEventTypesList: TypeAlias = list[
    "capo_mediatailor.types.manifest_service_exclude_event_type.ManifestServiceExcludeEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __manifestServiceExcludeEventTypesList) -> list:
    import capo_mediatailor.types.manifest_service_exclude_event_type

    out: list = []
    for item in value:
        out.append(
            capo_mediatailor.types.manifest_service_exclude_event_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __manifestServiceExcludeEventTypesList:
    import capo_mediatailor.types.manifest_service_exclude_event_type

    out: __manifestServiceExcludeEventTypesList = []
    for item in data:
        out.append(
            capo_mediatailor.types.manifest_service_exclude_event_type.deserialize_json(
                item
            )
        )
    return out
