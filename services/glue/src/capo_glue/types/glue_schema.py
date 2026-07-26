"""Generated from Smithy shape ``com.amazonaws.glue#GlueSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_studio_schema_column_list


class GlueSchema(TypedDict, closed=True):
    columns: NotRequired[
        "capo_glue.types.glue_studio_schema_column_list.GlueStudioSchemaColumnList"
    ]
    """<p>Specifies the column definitions that make up a Glue schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueSchema) -> dict:
    out: dict = {}
    if "columns" in value:
        import capo_glue.types.glue_studio_schema_column_list

        out["Columns"] = (
            capo_glue.types.glue_studio_schema_column_list.serialize_aws_json_1_1(
                value["columns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueSchema:
    out: GlueSchema = {}  # type: ignore[typeddict-item]
    if "Columns" in data:
        import capo_glue.types.glue_studio_schema_column_list

        out["columns"] = (
            capo_glue.types.glue_studio_schema_column_list.deserialize_aws_json_1_1(
                data["Columns"]
            )
        )
    return out
