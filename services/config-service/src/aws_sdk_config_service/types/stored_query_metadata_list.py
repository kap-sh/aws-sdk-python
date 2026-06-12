"""Generated from Smithy shape ``com.amazonaws.configservice#StoredQueryMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.stored_query_metadata

StoredQueryMetadataList: TypeAlias = list[
    "aws_sdk_config_service.types.stored_query_metadata.StoredQueryMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StoredQueryMetadataList) -> list:
    import aws_sdk_config_service.types.stored_query_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.stored_query_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StoredQueryMetadataList:
    import aws_sdk_config_service.types.stored_query_metadata

    out: StoredQueryMetadataList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.stored_query_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
