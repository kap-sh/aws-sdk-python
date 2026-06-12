"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListDomainsForPackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.max_results
    import aws_sdk_elasticsearch_service.types.next_token
    import aws_sdk_elasticsearch_service.types.package_id


class ListDomainsForPackageRequest(TypedDict):
    package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID"
    """<p>The package for which to list domains.</p>"""
    max_results: "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
    """<p>Limits results to a maximum number of domains.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsForPackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainsForPackageRequest:
    out: ListDomainsForPackageRequest = {}  # type: ignore[typeddict-item]
    return out
