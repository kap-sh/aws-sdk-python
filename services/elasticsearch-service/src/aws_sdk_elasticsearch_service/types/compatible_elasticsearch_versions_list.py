"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CompatibleElasticsearchVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.compatible_versions_map

CompatibleElasticsearchVersionsList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.compatible_versions_map.CompatibleVersionsMap"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleElasticsearchVersionsList) -> list:
    import aws_sdk_elasticsearch_service.types.compatible_versions_map

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.compatible_versions_map.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CompatibleElasticsearchVersionsList:
    import aws_sdk_elasticsearch_service.types.compatible_versions_map

    out: CompatibleElasticsearchVersionsList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.compatible_versions_map.deserialize_json(
                item
            )
        )
    return out
