"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#IssuesDetected``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.issue_detected

IssuesDetected: TypeAlias = list[
    "aws_sdk_transcribe_streaming.types.issue_detected.IssueDetected"
]


# --- restJson1 ser/de ---
def serialize_json(value: IssuesDetected) -> list:
    import aws_sdk_transcribe_streaming.types.issue_detected

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe_streaming.types.issue_detected.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IssuesDetected:
    import aws_sdk_transcribe_streaming.types.issue_detected

    out: IssuesDetected = []
    for item in data:
        out.append(
            aws_sdk_transcribe_streaming.types.issue_detected.deserialize_json(item)
        )
    return out
