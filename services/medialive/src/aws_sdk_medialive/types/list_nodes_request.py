"""Generated from Smithy shape ``com.amazonaws.medialive#ListNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListNodesRequest(TypedDict):
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster"""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    """The maximum number of items to return."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The token to retrieve the next page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNodesRequest:
    out: ListNodesRequest = {}  # type: ignore[typeddict-item]
    return out
