"""Generated from Smithy shape ``com.amazonaws.configservice#StoredQueryMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.stored_query_metadata

StoredQueryMetadataList: TypeAlias = list[
    "capo_config_service.types.stored_query_metadata.StoredQueryMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StoredQueryMetadataList) -> list:
    import capo_config_service.types.stored_query_metadata

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.stored_query_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StoredQueryMetadataList:
    import capo_config_service.types.stored_query_metadata

    out: StoredQueryMetadataList = []
    for item in data:
        out.append(
            capo_config_service.types.stored_query_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
