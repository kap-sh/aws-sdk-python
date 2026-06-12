"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSrtCallerSourceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.srt_caller_source_request

__listOfSrtCallerSourceRequest: TypeAlias = list[
    "aws_sdk_medialive.types.srt_caller_source_request.SrtCallerSourceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSrtCallerSourceRequest) -> list:
    import aws_sdk_medialive.types.srt_caller_source_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.srt_caller_source_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfSrtCallerSourceRequest:
    import aws_sdk_medialive.types.srt_caller_source_request

    out: __listOfSrtCallerSourceRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.srt_caller_source_request.deserialize_json(item)
        )
    return out
