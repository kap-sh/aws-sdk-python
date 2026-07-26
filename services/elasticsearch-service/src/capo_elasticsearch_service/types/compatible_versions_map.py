"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CompatibleVersionsMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.elasticsearch_version_list
    import capo_elasticsearch_service.types.elasticsearch_version_string


class CompatibleVersionsMap(TypedDict, closed=True):
    source_version: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    ]
    """<p>The current version of Elasticsearch on which a domain is.</p>"""
    target_versions: NotRequired[
        "capo_elasticsearch_service.types.elasticsearch_version_list.ElasticsearchVersionList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleVersionsMap) -> dict:
    out: dict = {}
    if "source_version" in value:
        out["SourceVersion"] = value["source_version"]
    if "target_versions" in value:
        import capo_elasticsearch_service.types.elasticsearch_version_list

        out["TargetVersions"] = (
            capo_elasticsearch_service.types.elasticsearch_version_list.serialize_json(
                value["target_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CompatibleVersionsMap:
    out: CompatibleVersionsMap = {}  # type: ignore[typeddict-item]
    if "SourceVersion" in data:
        out["source_version"] = data["SourceVersion"]
    if "TargetVersions" in data:
        import capo_elasticsearch_service.types.elasticsearch_version_list

        out["target_versions"] = (
            capo_elasticsearch_service.types.elasticsearch_version_list.deserialize_json(
                data["TargetVersions"]
            )
        )
    return out
