"""Generated from Smithy shape ``com.amazonaws.mediatailor#__manifestServicePublishOptInEventTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.manifest_service_publish_opt_in_event_type

__manifestServicePublishOptInEventTypesList: TypeAlias = list[
    "capo_mediatailor.types.manifest_service_publish_opt_in_event_type.ManifestServicePublishOptInEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __manifestServicePublishOptInEventTypesList) -> list:
    import capo_mediatailor.types.manifest_service_publish_opt_in_event_type

    out: list = []
    for item in value:
        out.append(
            capo_mediatailor.types.manifest_service_publish_opt_in_event_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __manifestServicePublishOptInEventTypesList:
    import capo_mediatailor.types.manifest_service_publish_opt_in_event_type

    out: __manifestServicePublishOptInEventTypesList = []
    for item in data:
        out.append(
            capo_mediatailor.types.manifest_service_publish_opt_in_event_type.deserialize_json(
                item
            )
        )
    return out
