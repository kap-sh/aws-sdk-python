"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelMLModelTransformJobOutput``."""

from typing_extensions import NotRequired, TypedDict


class CancelMLModelTransformJobOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>the status of the cancelation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMLModelTransformJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelMLModelTransformJobOutput:
    out: CancelMLModelTransformJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
