"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListElasticsearchInstanceTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_instance_type_list
    import aws_sdk_elasticsearch_service.types.next_token


class ListElasticsearchInstanceTypesResponse(TypedDict, closed=True):
    elasticsearch_instance_types: NotRequired[
        "aws_sdk_elasticsearch_service.types.elasticsearch_instance_type_list.ElasticsearchInstanceTypeList"
    ]
    """<p> List of instance types supported by Amazon Elasticsearch service for given <code> <a>ElasticsearchVersion</a> </code> </p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p>In case if there are more results available NextToken would be present, make further request to the same API with received NextToken to paginate remaining results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListElasticsearchInstanceTypesResponse) -> dict:
    out: dict = {}
    if "elasticsearch_instance_types" in value:
        import aws_sdk_elasticsearch_service.types.elasticsearch_instance_type_list

        out["ElasticsearchInstanceTypes"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_instance_type_list.serialize_json(
                value["elasticsearch_instance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListElasticsearchInstanceTypesResponse:
    out: ListElasticsearchInstanceTypesResponse = {}  # type: ignore[typeddict-item]
    if "ElasticsearchInstanceTypes" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_instance_type_list

        out["elasticsearch_instance_types"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_instance_type_list.deserialize_json(
                data["ElasticsearchInstanceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
