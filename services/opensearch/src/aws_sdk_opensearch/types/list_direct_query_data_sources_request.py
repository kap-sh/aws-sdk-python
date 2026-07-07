"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDirectQueryDataSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.next_token


class ListDirectQueryDataSourcesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDirectQueryDataSourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDirectQueryDataSourcesRequest:
    out: ListDirectQueryDataSourcesRequest = {}  # type: ignore[typeddict-item]
    return out
