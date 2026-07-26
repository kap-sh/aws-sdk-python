"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfSrtCallerSourceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.srt_caller_source_request

__listOfSrtCallerSourceRequest: TypeAlias = list[
    "capo_medialive.types.srt_caller_source_request.SrtCallerSourceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSrtCallerSourceRequest) -> list:
    import capo_medialive.types.srt_caller_source_request

    out: list = []
    for item in value:
        out.append(capo_medialive.types.srt_caller_source_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSrtCallerSourceRequest:
    import capo_medialive.types.srt_caller_source_request

    out: __listOfSrtCallerSourceRequest = []
    for item in data:
        out.append(
            capo_medialive.types.srt_caller_source_request.deserialize_json(item)
        )
    return out
