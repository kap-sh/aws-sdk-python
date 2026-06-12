"""Generated from Smithy shape ``com.amazonaws.ivs#PlaybackKeyPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_key_pair_summary

PlaybackKeyPairList: TypeAlias = list[
    "aws_sdk_ivs.types.playback_key_pair_summary.PlaybackKeyPairSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackKeyPairList) -> list:
    import aws_sdk_ivs.types.playback_key_pair_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.playback_key_pair_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlaybackKeyPairList:
    import aws_sdk_ivs.types.playback_key_pair_summary

    out: PlaybackKeyPairList = []
    for item in data:
        out.append(aws_sdk_ivs.types.playback_key_pair_summary.deserialize_json(item))
    return out
