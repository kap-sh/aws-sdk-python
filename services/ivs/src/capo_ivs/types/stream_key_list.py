"""Generated from Smithy shape ``com.amazonaws.ivs#StreamKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.stream_key_summary

StreamKeyList: TypeAlias = list["capo_ivs.types.stream_key_summary.StreamKeySummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamKeyList) -> list:
    import capo_ivs.types.stream_key_summary

    out: list = []
    for item in value:
        out.append(capo_ivs.types.stream_key_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamKeyList:
    import capo_ivs.types.stream_key_summary

    out: StreamKeyList = []
    for item in data:
        out.append(capo_ivs.types.stream_key_summary.deserialize_json(item))
    return out
