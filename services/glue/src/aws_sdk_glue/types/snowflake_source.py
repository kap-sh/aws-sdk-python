"""Generated from Smithy shape ``com.amazonaws.glue#SnowflakeSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.snowflake_node_data


class SnowflakeSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the Snowflake data source.</p>"""
    data: "aws_sdk_glue.types.snowflake_node_data.SnowflakeNodeData"
    """<p>Configuration for the Snowflake data source.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies user-defined schemas for your output data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.snowflake_node_data

    out["Data"] = aws_sdk_glue.types.snowflake_node_data.serialize_aws_json_1_1(
        value["data"]
    )
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeSource:
    out: SnowflakeSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SnowflakeSource.name required")
    if "Data" in data:
        import aws_sdk_glue.types.snowflake_node_data

        out["data"] = aws_sdk_glue.types.snowflake_node_data.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("SnowflakeSource.data required")
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
