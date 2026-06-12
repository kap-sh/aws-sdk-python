"""Generated from Smithy shape ``com.amazonaws.m2#ListDataSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token
    import aws_sdk_m2.types.string200


class ListDataSetsRequest(TypedDict):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application for which you want to list the associated data sets.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>"""
    max_results: NotRequired["aws_sdk_m2.types.max_results.MaxResults"]
    """<p>The maximum number of objects to return.</p>"""
    prefix: NotRequired["aws_sdk_m2.types.string200.String200"]
    """<p>The prefix of the data set name, which you can use to filter the list of data sets.</p>"""
    name_filter: NotRequired["aws_sdk_m2.types.string200.String200"]
    """<p>Filter dataset name matching the specified pattern. Can use * and % as wild cards.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSetsRequest:
    out: ListDataSetsRequest = {}  # type: ignore[typeddict-item]
    return out
