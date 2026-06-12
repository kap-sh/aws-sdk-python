"""Generated from Smithy shape ``com.amazonaws.glue#SnowflakeTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.snowflake_node_data


class SnowflakeTarget(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the Snowflake target.</p>"""
    data: "aws_sdk_glue.types.snowflake_node_data.SnowflakeNodeData"
    """<p>Specifies the data of the Snowflake target node.</p>"""
    inputs: NotRequired["aws_sdk_glue.types.one_input.OneInput"]
    """<p>The nodes that are inputs to the data target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.snowflake_node_data

    out["Data"] = aws_sdk_glue.types.snowflake_node_data.serialize_aws_json_1_1(
        value["data"]
    )
    if "inputs" in value:
        import aws_sdk_glue.types.one_input

        out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(
            value["inputs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeTarget:
    out: SnowflakeTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SnowflakeTarget.name required")
    if "Data" in data:
        import aws_sdk_glue.types.snowflake_node_data

        out["data"] = aws_sdk_glue.types.snowflake_node_data.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("SnowflakeTarget.data required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    return out
