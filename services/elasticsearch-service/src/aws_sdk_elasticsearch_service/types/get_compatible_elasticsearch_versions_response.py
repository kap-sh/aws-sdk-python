"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetCompatibleElasticsearchVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.compatible_elasticsearch_versions_list


class GetCompatibleElasticsearchVersionsResponse(TypedDict):
    compatible_elasticsearch_versions: NotRequired[
        "aws_sdk_elasticsearch_service.types.compatible_elasticsearch_versions_list.CompatibleElasticsearchVersionsList"
    ]
    """<p> A map of compatible Elasticsearch versions returned as part of the <code> <a>GetCompatibleElasticsearchVersions</a> </code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleElasticsearchVersionsResponse) -> dict:
    out: dict = {}
    if "compatible_elasticsearch_versions" in value:
        import aws_sdk_elasticsearch_service.types.compatible_elasticsearch_versions_list

        out["CompatibleElasticsearchVersions"] = (
            aws_sdk_elasticsearch_service.types.compatible_elasticsearch_versions_list.serialize_json(
                value["compatible_elasticsearch_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCompatibleElasticsearchVersionsResponse:
    out: GetCompatibleElasticsearchVersionsResponse = {}  # type: ignore[typeddict-item]
    if "CompatibleElasticsearchVersions" in data:
        import aws_sdk_elasticsearch_service.types.compatible_elasticsearch_versions_list

        out["compatible_elasticsearch_versions"] = (
            aws_sdk_elasticsearch_service.types.compatible_elasticsearch_versions_list.deserialize_json(
                data["CompatibleElasticsearchVersions"]
            )
        )
    return out
