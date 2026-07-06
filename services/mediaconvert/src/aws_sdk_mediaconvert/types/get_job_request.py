"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class GetJobRequest(TypedDict, closed=True):
    id: "aws_sdk_mediaconvert.types.__string.__string"
    """the job ID of the job."""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobRequest:
    out: GetJobRequest = {}  # type: ignore[typeddict-item]
    return out
