"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.request_metadata_base_filters

RequestMetadataFiltersList: TypeAlias = list[
    "aws_sdk_bedrock.types.request_metadata_base_filters.RequestMetadataBaseFilters"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadataFiltersList) -> list:
    import aws_sdk_bedrock.types.request_metadata_base_filters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.request_metadata_base_filters.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RequestMetadataFiltersList:
    import aws_sdk_bedrock.types.request_metadata_base_filters

    out: RequestMetadataFiltersList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.request_metadata_base_filters.deserialize_json(item)
        )
    return out
