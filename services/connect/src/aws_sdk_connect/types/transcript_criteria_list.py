"""Generated from Smithy shape ``com.amazonaws.connect#TranscriptCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.transcript_criteria

TranscriptCriteriaList: TypeAlias = list[
    "aws_sdk_connect.types.transcript_criteria.TranscriptCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptCriteriaList) -> list:
    import aws_sdk_connect.types.transcript_criteria

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.transcript_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> TranscriptCriteriaList:
    import aws_sdk_connect.types.transcript_criteria

    out: TranscriptCriteriaList = []
    for item in data:
        out.append(aws_sdk_connect.types.transcript_criteria.deserialize_json(item))
    return out
