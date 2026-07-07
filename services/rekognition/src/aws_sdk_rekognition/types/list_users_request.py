"""Generated from Smithy shape ``com.amazonaws.rekognition#ListUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.max_user_results
    import aws_sdk_rekognition.types.pagination_token


class ListUsersRequest(TypedDict, closed=True):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>The ID of an existing collection.</p>"""
    max_results: NotRequired[
        "aws_sdk_rekognition.types.max_user_results.MaxUserResults"
    ]
    """<p>Maximum number of UsersID to return. </p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>Pagingation token to receive the next set of UsersID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsersRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsersRequest:
    out: ListUsersRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("ListUsersRequest.collection_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
