"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AssociatedTranscriptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.associated_transcript

AssociatedTranscriptList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.associated_transcript.AssociatedTranscript"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTranscriptList) -> list:
    import aws_sdk_lex_models_v2.types.associated_transcript

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.associated_transcript.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedTranscriptList:
    import aws_sdk_lex_models_v2.types.associated_transcript

    out: AssociatedTranscriptList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.associated_transcript.deserialize_json(item)
        )
    return out
