"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListElasticsearchVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_list
    import aws_sdk_elasticsearch_service.types.next_token


class ListElasticsearchVersionsResponse(TypedDict, closed=True):
    elasticsearch_versions: NotRequired[
        "aws_sdk_elasticsearch_service.types.elasticsearch_version_list.ElasticsearchVersionList"
    ]
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListElasticsearchVersionsResponse) -> dict:
    out: dict = {}
    if "elasticsearch_versions" in value:
        import aws_sdk_elasticsearch_service.types.elasticsearch_version_list

        out["ElasticsearchVersions"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_version_list.serialize_json(
                value["elasticsearch_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListElasticsearchVersionsResponse:
    out: ListElasticsearchVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ElasticsearchVersions" in data:
        import aws_sdk_elasticsearch_service.types.elasticsearch_version_list

        out["elasticsearch_versions"] = (
            aws_sdk_elasticsearch_service.types.elasticsearch_version_list.deserialize_json(
                data["ElasticsearchVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
