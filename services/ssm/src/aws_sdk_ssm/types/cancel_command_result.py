"""Generated from Smithy shape ``com.amazonaws.ssm#CancelCommandResult``."""

from typing_extensions import TypedDict


class CancelCommandResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCommandResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCommandResult:
    out: CancelCommandResult = {}  # type: ignore[typeddict-item]
    return out
