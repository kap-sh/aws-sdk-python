"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSrtCallerSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.srt_caller_source

__listOfSrtCallerSource: TypeAlias = list[
    "aws_sdk_medialive.types.srt_caller_source.SrtCallerSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSrtCallerSource) -> list:
    import aws_sdk_medialive.types.srt_caller_source

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.srt_caller_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSrtCallerSource:
    import aws_sdk_medialive.types.srt_caller_source

    out: __listOfSrtCallerSource = []
    for item in data:
        out.append(aws_sdk_medialive.types.srt_caller_source.deserialize_json(item))
    return out
