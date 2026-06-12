"""Generated from Smithy shape ``com.amazonaws.m2#ListEngineVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token


class ListEngineVersionsRequest(TypedDict):
    engine_type: NotRequired["aws_sdk_m2.types.engine_type.EngineType"]
    """<p>The type of target platform.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>"""
    max_results: NotRequired["aws_sdk_m2.types.max_results.MaxResults"]
    """<p>The maximum number of objects to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEngineVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEngineVersionsRequest:
    out: ListEngineVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
