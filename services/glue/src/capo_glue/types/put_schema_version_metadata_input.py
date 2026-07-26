"""Generated from Smithy shape ``com.amazonaws.glue#PutSchemaVersionMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.metadata_key_value_pair
    import capo_glue.types.schema_id
    import capo_glue.types.schema_version_id_string
    import capo_glue.types.schema_version_number


class PutSchemaVersionMetadataInput(TypedDict, closed=True):
    schema_id: NotRequired["capo_glue.types.schema_id.SchemaId"]
    """<p>The unique ID for the schema.</p>"""
    schema_version_number: NotRequired[
        "capo_glue.types.schema_version_number.SchemaVersionNumber"
    ]
    """<p>The version number of the schema.</p>"""
    schema_version_id: NotRequired[
        "capo_glue.types.schema_version_id_string.SchemaVersionIdString"
    ]
    """<p>The unique version ID of the schema version.</p>"""
    metadata_key_value: "capo_glue.types.metadata_key_value_pair.MetadataKeyValuePair"
    """<p>The metadata key's corresponding value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSchemaVersionMetadataInput) -> dict:
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
    import capo_glue.types.metadata_key_value_pair

    out["MetadataKeyValue"] = (
        capo_glue.types.metadata_key_value_pair.serialize_aws_json_1_1(
            value["metadata_key_value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSchemaVersionMetadataInput:
    out: PutSchemaVersionMetadataInput = {}  # type: ignore[typeddict-item]
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
    if "MetadataKeyValue" in data:
        import capo_glue.types.metadata_key_value_pair

        out["metadata_key_value"] = (
            capo_glue.types.metadata_key_value_pair.deserialize_aws_json_1_1(
                data["MetadataKeyValue"]
            )
        )
    else:
        raise DeserializationError(
            "PutSchemaVersionMetadataInput.metadata_key_value required"
        )
    return out
