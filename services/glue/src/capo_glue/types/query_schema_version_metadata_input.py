"""Generated from Smithy shape ``com.amazonaws.glue#QuerySchemaVersionMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.metadata_list
    import capo_glue.types.query_schema_version_metadata_max_results
    import capo_glue.types.schema_id
    import capo_glue.types.schema_registry_token_string
    import capo_glue.types.schema_version_id_string
    import capo_glue.types.schema_version_number


class QuerySchemaVersionMetadataInput(TypedDict, closed=True):
    schema_id: NotRequired["capo_glue.types.schema_id.SchemaId"]
    """<p>A wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>"""
    schema_version_number: NotRequired[
        "capo_glue.types.schema_version_number.SchemaVersionNumber"
    ]
    """<p>The version number of the schema.</p>"""
    schema_version_id: NotRequired[
        "capo_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique version ID of the schema version.</p>"""
    metadata_list: NotRequired["capo_glue.types.metadata_list.MetadataList"]
    """<p>Search key-value pairs for metadata, if they are not provided all the metadata information will be fetched.</p>"""
    max_results: NotRequired[
        "capo_glue.types.query_schema_version_metadata_max_results.QuerySchemaVersionMetadataMaxResults"
    ]
    """<p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>"""
    next_token: NotRequired[
        "capo_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuerySchemaVersionMetadataInput) -> dict:
    out: dict = {}
    if "schema_id" in value:
        import capo_glue.types.schema_id

        out["SchemaId"] = capo_glue.types.schema_id.serialize_aws_json_1_1(
            value["schema_id"]
        )
    if "schema_version_number" in value:
        import capo_glue.types.schema_version_number

        out["SchemaVersionNumber"] = (
            capo_glue.types.schema_version_number.serialize_aws_json_1_1(
                value["schema_version_number"]
            )
        )
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    if "metadata_list" in value:
        import capo_glue.types.metadata_list

        out["MetadataList"] = capo_glue.types.metadata_list.serialize_aws_json_1_1(
            value["metadata_list"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QuerySchemaVersionMetadataInput:
    out: QuerySchemaVersionMetadataInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import capo_glue.types.schema_id

        out["schema_id"] = capo_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    if "SchemaVersionNumber" in data:
        import capo_glue.types.schema_version_number

        out["schema_version_number"] = (
            capo_glue.types.schema_version_number.deserialize_aws_json_1_1(
                data["SchemaVersionNumber"]
            )
        )
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "MetadataList" in data:
        import capo_glue.types.metadata_list

        out["metadata_list"] = capo_glue.types.metadata_list.deserialize_aws_json_1_1(
            data["MetadataList"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
