"""Generated from Smithy shape ``com.amazonaws.rekognition#ListCollectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.page_size
    import aws_sdk_rekognition.types.pagination_token


class ListCollectionsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_rekognition.types.page_size.PageSize"]
    """<p>Maximum number of collection IDs to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCollectionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCollectionsRequest:
    out: ListCollectionsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
