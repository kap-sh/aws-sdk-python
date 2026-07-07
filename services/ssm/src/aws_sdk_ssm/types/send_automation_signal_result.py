"""Generated from Smithy shape ``com.amazonaws.ssm#SendAutomationSignalResult``."""

from typing_extensions import TypedDict


class SendAutomationSignalResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendAutomationSignalResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> SendAutomationSignalResult:
    out: SendAutomationSignalResult = {}  # type: ignore[typeddict-item]
    return out
