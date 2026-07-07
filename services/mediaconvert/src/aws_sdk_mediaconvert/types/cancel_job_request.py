"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CancelJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class CancelJobRequest(TypedDict, closed=True):
    id: "aws_sdk_mediaconvert.types.__string.__string"
    """The Job ID of the job to be cancelled."""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    return out
