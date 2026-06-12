"""Generated from Smithy shape ``com.amazonaws.glue#GlueSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_studio_schema_column_list


class GlueSchema(TypedDict):
    columns: NotRequired[
        "aws_sdk_glue.types.glue_studio_schema_column_list.GlueStudioSchemaColumnList"
    ]
    """<p>Specifies the column definitions that make up a Glue schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueSchema) -> dict:
    out: dict = {}
    if "columns" in value:
        import aws_sdk_glue.types.glue_studio_schema_column_list

        out["Columns"] = (
            aws_sdk_glue.types.glue_studio_schema_column_list.serialize_aws_json_1_1(
                value["columns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueSchema:
    out: GlueSchema = {}  # type: ignore[typeddict-item]
    if "Columns" in data:
        import aws_sdk_glue.types.glue_studio_schema_column_list

        out["columns"] = (
            aws_sdk_glue.types.glue_studio_schema_column_list.deserialize_aws_json_1_1(
                data["Columns"]
            )
        )
    return out
