"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.channel_summary

__listOfChannelSummary: TypeAlias = list[
    "capo_medialive.types.channel_summary.ChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelSummary) -> list:
    import capo_medialive.types.channel_summary

    out: list = []
    for item in value:
        out.append(capo_medialive.types.channel_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannelSummary:
    import capo_medialive.types.channel_summary

    out: __listOfChannelSummary = []
    for item in data:
        out.append(capo_medialive.types.channel_summary.deserialize_json(item))
    return out
