"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListMediaCapturePipelinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.result_max
    import aws_sdk_chime_sdk_media_pipelines.types.string


class ListMediaCapturePipelinesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.string.String"]
    """<p>The token used to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.result_max.ResultMax"
    ]
    """<p>The maximum number of results to return in a single call. Valid Range: 1 - 99.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMediaCapturePipelinesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMediaCapturePipelinesRequest:
    out: ListMediaCapturePipelinesRequest = {}  # type: ignore[typeddict-item]
    return out
