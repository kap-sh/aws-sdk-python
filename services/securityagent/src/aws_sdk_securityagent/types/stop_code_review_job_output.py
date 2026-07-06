"""Generated from Smithy shape ``com.amazonaws.securityagent#StopCodeReviewJobOutput``."""

from typing_extensions import TypedDict


class StopCodeReviewJobOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopCodeReviewJobOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopCodeReviewJobOutput:
    out: StopCodeReviewJobOutput = {}  # type: ignore[typeddict-item]
    return out
