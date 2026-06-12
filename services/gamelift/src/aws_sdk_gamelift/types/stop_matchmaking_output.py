"""Generated from Smithy shape ``com.amazonaws.gamelift#StopMatchmakingOutput``."""

from typing import TypedDict


class StopMatchmakingOutput(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopMatchmakingOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopMatchmakingOutput:
    out: StopMatchmakingOutput = {}  # type: ignore[typeddict-item]
    return out
