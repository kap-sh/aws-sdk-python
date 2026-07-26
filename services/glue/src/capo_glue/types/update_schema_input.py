"""Generated from Smithy shape ``com.amazonaws.glue#UpdateSchemaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.compatibility
    import capo_glue.types.description_string
    import capo_glue.types.schema_id
    import capo_glue.types.schema_version_number


class UpdateSchemaInput(TypedDict, closed=True):
    schema_id: "capo_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> </ul>"""
    schema_version_number: NotRequired[
        "capo_glue.types.schema_version_number.SchemaVersionNumber"
    ]
    """<p>Version number required for check pointing. One of <code>VersionNumber</code> or <code>Compatibility</code> has to be provided.</p>"""
    compatibility: NotRequired["capo_glue.types.compatibility.Compatibility"]
    """<p>The new compatibility setting for the schema.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The new description for the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSchemaInput) -> dict:
    out: dict = {}
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
    if "compatibility" in value:
        import capo_glue.types.compatibility

        out["Compatibility"] = capo_glue.types.compatibility.serialize_aws_json_1_1(
            value["compatibility"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSchemaInput:
    out: UpdateSchemaInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import capo_glue.types.schema_id

        out["schema_id"] = capo_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("UpdateSchemaInput.schema_id required")
    if "SchemaVersionNumber" in data:
        import capo_glue.types.schema_version_number

        out["schema_version_number"] = (
            capo_glue.types.schema_version_number.deserialize_aws_json_1_1(
                data["SchemaVersionNumber"]
            )
        )
    if "Compatibility" in data:
        import capo_glue.types.compatibility

        out["compatibility"] = capo_glue.types.compatibility.deserialize_aws_json_1_1(
            data["Compatibility"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
