"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.result

ResultList: TypeAlias = list["aws_sdk_transcribe_streaming.types.result.Result"]


# --- restJson1 ser/de ---
def serialize_json(value: ResultList) -> list:
    import aws_sdk_transcribe_streaming.types.result

    out: list = []
    for item in value:
        out.append(aws_sdk_transcribe_streaming.types.result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResultList:
    import aws_sdk_transcribe_streaming.types.result

    out: ResultList = []
    for item in data:
        out.append(aws_sdk_transcribe_streaming.types.result.deserialize_json(item))
    return out
