"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelMLDataProcessingJobOutput``."""

from typing_extensions import NotRequired, TypedDict


class CancelMLDataProcessingJobOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>The status of the cancellation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMLDataProcessingJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelMLDataProcessingJobOutput:
    out: CancelMLDataProcessingJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
