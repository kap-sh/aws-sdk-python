"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSrtCallerSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.srt_caller_source

__listOfSrtCallerSource: TypeAlias = list[
    "capo_medialive.types.srt_caller_source.SrtCallerSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSrtCallerSource) -> list:
    import capo_medialive.types.srt_caller_source

    out: list = []
    for item in value:
        out.append(capo_medialive.types.srt_caller_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSrtCallerSource:
    import capo_medialive.types.srt_caller_source

    out: __listOfSrtCallerSource = []
    for item in data:
        out.append(capo_medialive.types.srt_caller_source.deserialize_json(item))
    return out
