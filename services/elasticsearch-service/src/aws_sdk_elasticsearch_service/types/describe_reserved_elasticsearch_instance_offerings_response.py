"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeReservedElasticsearchInstanceOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.next_token
    import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering_list


class DescribeReservedElasticsearchInstanceOfferingsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    reserved_elasticsearch_instance_offerings: NotRequired[
        "aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering_list.ReservedElasticsearchInstanceOfferingList"
    ]
    """<p>List of reserved Elasticsearch instance offerings</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DescribeReservedElasticsearchInstanceOfferingsResponse,
) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_elasticsearch_instance_offerings" in value:
        import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering_list

        out["ReservedElasticsearchInstanceOfferings"] = (
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering_list.serialize_json(
                value["reserved_elasticsearch_instance_offerings"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> DescribeReservedElasticsearchInstanceOfferingsResponse:
    out: DescribeReservedElasticsearchInstanceOfferingsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ReservedElasticsearchInstanceOfferings" in data:
        import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering_list

        out["reserved_elasticsearch_instance_offerings"] = (
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_offering_list.deserialize_json(
                data["ReservedElasticsearchInstanceOfferings"]
            )
        )
    return out
