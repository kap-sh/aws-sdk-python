"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeReservedElasticsearchInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_list
    import aws_sdk_elasticsearch_service.types.string


class DescribeReservedElasticsearchInstancesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    reserved_elasticsearch_instances: NotRequired[
        "aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_list.ReservedElasticsearchInstanceList"
    ]
    """<p>List of reserved Elasticsearch instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservedElasticsearchInstancesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_elasticsearch_instances" in value:
        import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_list

        out["ReservedElasticsearchInstances"] = (
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_list.serialize_json(
                value["reserved_elasticsearch_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeReservedElasticsearchInstancesResponse:
    out: DescribeReservedElasticsearchInstancesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ReservedElasticsearchInstances" in data:
        import aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_list

        out["reserved_elasticsearch_instances"] = (
            aws_sdk_elasticsearch_service.types.reserved_elasticsearch_instance_list.deserialize_json(
                data["ReservedElasticsearchInstances"]
            )
        )
    return out
