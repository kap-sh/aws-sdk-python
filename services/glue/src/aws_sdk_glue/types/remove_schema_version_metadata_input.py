"""Generated from Smithy shape ``com.amazonaws.glue#RemoveSchemaVersionMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.metadata_key_value_pair
    import aws_sdk_glue.types.schema_id
    import aws_sdk_glue.types.schema_version_id_string
    import aws_sdk_glue.types.schema_version_number


class RemoveSchemaVersionMetadataInput(TypedDict):
    schema_id: NotRequired["aws_sdk_glue.types.schema_id.SchemaId"]
    """<p>A wrapper structure that may contain the schema name and Amazon Resource Name (ARN).</p>"""
    schema_version_number: NotRequired[
        "aws_sdk_glue.types.schema_version_number.SchemaVersionNumber"
    ]
    """<p>The version number of the schema.</p>"""
    schema_version_id: NotRequired[
        "aws_sdk_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique version ID of the schema version.</p>"""
    metadata_key_value: (
        "aws_sdk_glue.types.metadata_key_value_pair.MetadataKeyValuePair"
    )
    """<p>The value of the metadata key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveSchemaVersionMetadataInput) -> dict:
    out: dict = {}
    if "schema_id" in value:
        import aws_sdk_glue.types.schema_id

        out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
            value["schema_id"]
        )
    if "schema_version_number" in value:
        import aws_sdk_glue.types.schema_version_number

        out["SchemaVersionNumber"] = (
            aws_sdk_glue.types.schema_version_number.serialize_aws_json_1_1(
                value["schema_version_number"]
            )
        )
    if "schema_version_id" in value:
        out["SchemaVersionId"] = value["schema_version_id"]
    import aws_sdk_glue.types.metadata_key_value_pair

    out["MetadataKeyValue"] = (
        aws_sdk_glue.types.metadata_key_value_pair.serialize_aws_json_1_1(
            value["metadata_key_value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveSchemaVersionMetadataInput:
    out: RemoveSchemaVersionMetadataInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    if "SchemaVersionNumber" in data:
        import aws_sdk_glue.types.schema_version_number

        out["schema_version_number"] = (
            aws_sdk_glue.types.schema_version_number.deserialize_aws_json_1_1(
                data["SchemaVersionNumber"]
            )
        )
    if "SchemaVersionId" in data:
        out["schema_version_id"] = data["SchemaVersionId"]
    if "MetadataKeyValue" in data:
        import aws_sdk_glue.types.metadata_key_value_pair

        out["metadata_key_value"] = (
            aws_sdk_glue.types.metadata_key_value_pair.deserialize_aws_json_1_1(
                data["MetadataKeyValue"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveSchemaVersionMetadataInput.metadata_key_value required"
        )
    return out
