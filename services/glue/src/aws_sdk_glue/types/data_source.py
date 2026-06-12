"""Generated from Smithy shape ``com.amazonaws.glue#DataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_glue_table
    import aws_sdk_glue.types.glue_table


class DataSource(TypedDict):
    glue_table: NotRequired["aws_sdk_glue.types.glue_table.GlueTable"]
    """<p>An Glue table.</p>"""
    data_quality_glue_table: NotRequired[
        "aws_sdk_glue.types.data_quality_glue_table.DataQualityGlueTable"
    ]
    """<p>An Glue table for Data Quality Operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
    out: dict = {}
    if "glue_table" in value:
        import aws_sdk_glue.types.glue_table

        out["GlueTable"] = aws_sdk_glue.types.glue_table.serialize_aws_json_1_1(
            value["glue_table"]
        )
    if "data_quality_glue_table" in value:
        import aws_sdk_glue.types.data_quality_glue_table

        out["DataQualityGlueTable"] = (
            aws_sdk_glue.types.data_quality_glue_table.serialize_aws_json_1_1(
                value["data_quality_glue_table"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "GlueTable" in data:
        import aws_sdk_glue.types.glue_table

        out["glue_table"] = aws_sdk_glue.types.glue_table.deserialize_aws_json_1_1(
            data["GlueTable"]
        )
    if "DataQualityGlueTable" in data:
        import aws_sdk_glue.types.data_quality_glue_table

        out["data_quality_glue_table"] = (
            aws_sdk_glue.types.data_quality_glue_table.deserialize_aws_json_1_1(
                data["DataQualityGlueTable"]
            )
        )
    return out
