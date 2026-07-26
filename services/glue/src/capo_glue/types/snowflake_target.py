"""Generated from Smithy shape ``com.amazonaws.glue#SnowflakeTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.node_name
    import capo_glue.types.one_input
    import capo_glue.types.snowflake_node_data


class SnowflakeTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Snowflake target.</p>"""
    data: "capo_glue.types.snowflake_node_data.SnowflakeNodeData"
    """<p>Specifies the data of the Snowflake target node.</p>"""
    inputs: NotRequired["capo_glue.types.one_input.OneInput"]
    """<p>The nodes that are inputs to the data target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.snowflake_node_data

    out["Data"] = capo_glue.types.snowflake_node_data.serialize_aws_json_1_1(
        value["data"]
    )
    if "inputs" in value:
        import capo_glue.types.one_input

        out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(
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
        import capo_glue.types.snowflake_node_data

        out["data"] = capo_glue.types.snowflake_node_data.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("SnowflakeTarget.data required")
    if "Inputs" in data:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    return out
