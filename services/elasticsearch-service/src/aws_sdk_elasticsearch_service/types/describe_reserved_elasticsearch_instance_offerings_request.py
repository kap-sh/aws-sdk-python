"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeReservedElasticsearchInstanceOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.guid
    import aws_sdk_elasticsearch_service.types.max_results
    import aws_sdk_elasticsearch_service.types.next_token


class DescribeReservedElasticsearchInstanceOfferingsRequest(TypedDict):
    reserved_elasticsearch_instance_offering_id: NotRequired[
        "aws_sdk_elasticsearch_service.types.guid.GUID"
    ]
    """<p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>"""
    max_results: "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
    """<p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DescribeReservedElasticsearchInstanceOfferingsRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> DescribeReservedElasticsearchInstanceOfferingsRequest:
    out: DescribeReservedElasticsearchInstanceOfferingsRequest = {}  # type: ignore[typeddict-item]
    return out
