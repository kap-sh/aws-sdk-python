"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetCompatibleElasticsearchVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.compatible_elasticsearch_versions_list


class GetCompatibleElasticsearchVersionsResponse(TypedDict, closed=True):
    compatible_elasticsearch_versions: NotRequired[
        "capo_elasticsearch_service.types.compatible_elasticsearch_versions_list.CompatibleElasticsearchVersionsList"
    ]
    """<p> A map of compatible Elasticsearch versions returned as part of the <code> <a>GetCompatibleElasticsearchVersions</a> </code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleElasticsearchVersionsResponse) -> dict:
    out: dict = {}
    if "compatible_elasticsearch_versions" in value:
        import capo_elasticsearch_service.types.compatible_elasticsearch_versions_list

        out["CompatibleElasticsearchVersions"] = (
            capo_elasticsearch_service.types.compatible_elasticsearch_versions_list.serialize_json(
                value["compatible_elasticsearch_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCompatibleElasticsearchVersionsResponse:
    out: GetCompatibleElasticsearchVersionsResponse = {}  # type: ignore[typeddict-item]
    if "CompatibleElasticsearchVersions" in data:
        import capo_elasticsearch_service.types.compatible_elasticsearch_versions_list

        out["compatible_elasticsearch_versions"] = (
            capo_elasticsearch_service.types.compatible_elasticsearch_versions_list.deserialize_json(
                data["CompatibleElasticsearchVersions"]
            )
        )
    return out
