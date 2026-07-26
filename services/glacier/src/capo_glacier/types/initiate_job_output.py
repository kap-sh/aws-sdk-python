"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.string


class InitiateJobOutput(TypedDict, closed=True):
    location: NotRequired["capo_glacier.types.string.string"]
    """<p>The relative URI path of the job.</p>"""
    job_id: NotRequired["capo_glacier.types.string.string"]
    """<p>The ID of the job.</p>"""
    job_output_path: NotRequired["capo_glacier.types.string.string"]
    """<p>The path to the location of where the select results are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateJobOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InitiateJobOutput:
    out: InitiateJobOutput = {}  # type: ignore[typeddict-item]
    return out
