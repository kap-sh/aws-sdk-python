"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#AlternativeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.alternative

AlternativeList: TypeAlias = list[
    "aws_sdk_transcribe_streaming.types.alternative.Alternative"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlternativeList) -> list:
    import aws_sdk_transcribe_streaming.types.alternative

    out: list = []
    for item in value:
        out.append(aws_sdk_transcribe_streaming.types.alternative.serialize_json(item))
    return out


def deserialize_json(data: list) -> AlternativeList:
    import aws_sdk_transcribe_streaming.types.alternative

    out: AlternativeList = []
    for item in data:
        out.append(
            aws_sdk_transcribe_streaming.types.alternative.deserialize_json(item)
        )
    return out
