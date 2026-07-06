"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max20
    import aws_sdk_mediaconvert.types.__string


class ListVersionsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
    ]
    """Optional. Number of valid Job engine versions, up to twenty, that will be returned at one time."""
    next_token: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. Use this string, provided with the response to a previous request, to request the next batch of Job engine versions."""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVersionsRequest:
    out: ListVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
