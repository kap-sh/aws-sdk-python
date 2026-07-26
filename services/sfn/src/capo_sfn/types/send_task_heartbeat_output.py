"""Generated from Smithy shape ``com.amazonaws.sfn#SendTaskHeartbeatOutput``."""

from typing_extensions import TypedDict


class SendTaskHeartbeatOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendTaskHeartbeatOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> SendTaskHeartbeatOutput:
    out: SendTaskHeartbeatOutput = {}  # type: ignore[typeddict-item]
    return out
