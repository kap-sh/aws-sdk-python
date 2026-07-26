"""Generated from Smithy shape ``com.amazonaws.sesv2#TopicPreferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.topic_preference

TopicPreferenceList: TypeAlias = list[
    "capo_sesv2.types.topic_preference.TopicPreference"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicPreferenceList) -> list:
    import capo_sesv2.types.topic_preference

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.topic_preference.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicPreferenceList:
    import capo_sesv2.types.topic_preference

    out: TopicPreferenceList = []
    for item in data:
        out.append(capo_sesv2.types.topic_preference.deserialize_json(item))
    return out
