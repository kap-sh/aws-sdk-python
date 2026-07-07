"""Generated from Smithy shape ``com.amazonaws.iot#ListJobTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.laser_max_results
    import aws_sdk_iot.types.next_token


class ListJobTemplatesRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_iot.types.laser_max_results.LaserMaxResults"]
    """<p>The maximum number of results to return in the list.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to return the next set of results in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobTemplatesRequest:
    out: ListJobTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
