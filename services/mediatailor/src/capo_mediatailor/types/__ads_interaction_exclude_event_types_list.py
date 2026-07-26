"""Generated from Smithy shape ``com.amazonaws.mediatailor#__adsInteractionExcludeEventTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.ads_interaction_exclude_event_type

__adsInteractionExcludeEventTypesList: TypeAlias = list[
    "capo_mediatailor.types.ads_interaction_exclude_event_type.AdsInteractionExcludeEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __adsInteractionExcludeEventTypesList) -> list:
    import capo_mediatailor.types.ads_interaction_exclude_event_type

    out: list = []
    for item in value:
        out.append(
            capo_mediatailor.types.ads_interaction_exclude_event_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __adsInteractionExcludeEventTypesList:
    import capo_mediatailor.types.ads_interaction_exclude_event_type

    out: __adsInteractionExcludeEventTypesList = []
    for item in data:
        out.append(
            capo_mediatailor.types.ads_interaction_exclude_event_type.deserialize_json(
                item
            )
        )
    return out
