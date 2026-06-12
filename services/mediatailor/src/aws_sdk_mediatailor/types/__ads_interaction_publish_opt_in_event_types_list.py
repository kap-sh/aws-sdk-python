"""Generated from Smithy shape ``com.amazonaws.mediatailor#__adsInteractionPublishOptInEventTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.ads_interaction_publish_opt_in_event_type

__adsInteractionPublishOptInEventTypesList: TypeAlias = list[
    "aws_sdk_mediatailor.types.ads_interaction_publish_opt_in_event_type.AdsInteractionPublishOptInEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __adsInteractionPublishOptInEventTypesList) -> list:
    import aws_sdk_mediatailor.types.ads_interaction_publish_opt_in_event_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediatailor.types.ads_interaction_publish_opt_in_event_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __adsInteractionPublishOptInEventTypesList:
    import aws_sdk_mediatailor.types.ads_interaction_publish_opt_in_event_type

    out: __adsInteractionPublishOptInEventTypesList = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.ads_interaction_publish_opt_in_event_type.deserialize_json(
                item
            )
        )
    return out
