"""Generated from Smithy shape ``com.amazonaws.connect#PotentialAudioQualityIssues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.potential_audio_quality_issue

PotentialAudioQualityIssues: TypeAlias = list[
    "aws_sdk_connect.types.potential_audio_quality_issue.PotentialAudioQualityIssue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PotentialAudioQualityIssues) -> list:
    return list(value)


def deserialize_json(data: list) -> PotentialAudioQualityIssues:
    return list(data)
