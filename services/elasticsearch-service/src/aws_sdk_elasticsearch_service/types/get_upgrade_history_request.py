"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetUpgradeHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.max_results
    import aws_sdk_elasticsearch_service.types.next_token


class GetUpgradeHistoryRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    max_results: "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeHistoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUpgradeHistoryRequest:
    out: GetUpgradeHistoryRequest = {}  # type: ignore[typeddict-item]
    return out
