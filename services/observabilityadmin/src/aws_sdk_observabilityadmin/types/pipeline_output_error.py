"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PipelineOutputError``."""

from typing import TypedDict

from typing_extensions import NotRequired


class PipelineOutputError(TypedDict):
    message: NotRequired["str"]
    """<p>The detailed error message describing what went wrong during the pipeline test operation for this record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineOutputError) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PipelineOutputError:
    out: PipelineOutputError = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
