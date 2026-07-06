"""Generated from Smithy shape ``com.amazonaws.mediatailor#ManifestServiceInteractionLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__manifest_service_exclude_event_types_list
    import aws_sdk_mediatailor.types.__manifest_service_publish_opt_in_event_types_list


class ManifestServiceInteractionLog(TypedDict, closed=True):
    publish_opt_in_event_types: NotRequired[
        "aws_sdk_mediatailor.types.__manifest_service_publish_opt_in_event_types_list.__manifestServicePublishOptInEventTypesList"
    ]
    """<p>Indicates that MediaTailor will emit the selected events in the logs for playback sessions that are initialized with this configuration. These events are not emitted by default and must be explicitly opted in.</p>"""
    exclude_event_types: NotRequired[
        "aws_sdk_mediatailor.types.__manifest_service_exclude_event_types_list.__manifestServiceExcludeEventTypesList"
    ]
    """<p>Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManifestServiceInteractionLog) -> dict:
    out: dict = {}
    if "publish_opt_in_event_types" in value:
        import aws_sdk_mediatailor.types.__manifest_service_publish_opt_in_event_types_list

        out["PublishOptInEventTypes"] = (
            aws_sdk_mediatailor.types.__manifest_service_publish_opt_in_event_types_list.serialize_json(
                value["publish_opt_in_event_types"]
            )
        )
    if "exclude_event_types" in value:
        import aws_sdk_mediatailor.types.__manifest_service_exclude_event_types_list

        out["ExcludeEventTypes"] = (
            aws_sdk_mediatailor.types.__manifest_service_exclude_event_types_list.serialize_json(
                value["exclude_event_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManifestServiceInteractionLog:
    out: ManifestServiceInteractionLog = {}  # type: ignore[typeddict-item]
    if "PublishOptInEventTypes" in data:
        import aws_sdk_mediatailor.types.__manifest_service_publish_opt_in_event_types_list

        out["publish_opt_in_event_types"] = (
            aws_sdk_mediatailor.types.__manifest_service_publish_opt_in_event_types_list.deserialize_json(
                data["PublishOptInEventTypes"]
            )
        )
    if "ExcludeEventTypes" in data:
        import aws_sdk_mediatailor.types.__manifest_service_exclude_event_types_list

        out["exclude_event_types"] = (
            aws_sdk_mediatailor.types.__manifest_service_exclude_event_types_list.deserialize_json(
                data["ExcludeEventTypes"]
            )
        )
    return out
