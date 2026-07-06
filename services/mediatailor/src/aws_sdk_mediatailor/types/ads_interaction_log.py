"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsInteractionLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__ads_interaction_exclude_event_types_list
    import aws_sdk_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list


class AdsInteractionLog(TypedDict, closed=True):
    publish_opt_in_event_types: NotRequired[
        "aws_sdk_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list.__adsInteractionPublishOptInEventTypesList"
    ]
    """<p>Indicates that MediaTailor emits <code>RAW_ADS_RESPONSE</code> logs for playback sessions that are initialized with this configuration.</p>"""
    exclude_event_types: NotRequired[
        "aws_sdk_mediatailor.types.__ads_interaction_exclude_event_types_list.__adsInteractionExcludeEventTypesList"
    ]
    """<p>Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdsInteractionLog) -> dict:
    out: dict = {}
    if "publish_opt_in_event_types" in value:
        import aws_sdk_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list

        out["PublishOptInEventTypes"] = (
            aws_sdk_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list.serialize_json(
                value["publish_opt_in_event_types"]
            )
        )
    if "exclude_event_types" in value:
        import aws_sdk_mediatailor.types.__ads_interaction_exclude_event_types_list

        out["ExcludeEventTypes"] = (
            aws_sdk_mediatailor.types.__ads_interaction_exclude_event_types_list.serialize_json(
                value["exclude_event_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdsInteractionLog:
    out: AdsInteractionLog = {}  # type: ignore[typeddict-item]
    if "PublishOptInEventTypes" in data:
        import aws_sdk_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list

        out["publish_opt_in_event_types"] = (
            aws_sdk_mediatailor.types.__ads_interaction_publish_opt_in_event_types_list.deserialize_json(
                data["PublishOptInEventTypes"]
            )
        )
    if "ExcludeEventTypes" in data:
        import aws_sdk_mediatailor.types.__ads_interaction_exclude_event_types_list

        out["exclude_event_types"] = (
            aws_sdk_mediatailor.types.__ads_interaction_exclude_event_types_list.deserialize_json(
                data["ExcludeEventTypes"]
            )
        )
    return out
