"""Generated from Smithy shape ``com.amazonaws.mediaconvert#StartJobsQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class StartJobsQueryResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The ID of the jobs query."""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobsQueryResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> StartJobsQueryResponse:
    out: StartJobsQueryResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
