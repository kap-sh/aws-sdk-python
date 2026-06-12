"""Generated from Smithy shape ``com.amazonaws.glue#QuerySchemaVersionMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.metadata_info_map
    import aws_sdk_glue.types.schema_registry_token_string
    import aws_sdk_glue.types.schema_version_id_string


class QuerySchemaVersionMetadataResponse(TypedDict):
    metadata_info_map: NotRequired[
        "aws_sdk_glue.types.metadata_info_map.MetadataInfoMap"
    ]
    """<p>A map of a metadata key and associated values.</p>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique version ID of the schema version.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySchemaVersionMetadataResponse) -> dict:
    out: dict = {}
    if "metadata_info_map" in value:
        import aws_sdk_glue.types.metadata_info_map

        out["MetadataInfoMap"] = (
            aws_sdk_glue.types.metadata_info_map.serialize_aws_json_1_1(
                value["metadata_info_map"]
            )
        )
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QuerySchemaVersionMetadataResponse:
    out: QuerySchemaVersionMetadataResponse = {}  # type: ignore[typeddict-item]
    if "MetadataInfoMap" in data:
        import aws_sdk_glue.types.metadata_info_map

        out["metadata_info_map"] = (
            aws_sdk_glue.types.metadata_info_map.deserialize_aws_json_1_1(
                data["MetadataInfoMap"]
            )
        )
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
