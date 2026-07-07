"""Generated from Smithy shape ``com.amazonaws.glue#AmazonRedshiftTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.amazon_redshift_node_data
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class AmazonRedshiftTarget(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.node_name.NodeName"]
    """<p>The name of the Amazon Redshift target.</p>"""
    data: NotRequired[
        "aws_sdk_glue.types.amazon_redshift_node_data.AmazonRedshiftNodeData"
    ]
    """<p>Specifies the data of the Amazon Redshift target node.</p>"""
    inputs: NotRequired["aws_sdk_glue.types.one_input.OneInput"]
    """<p>The nodes that are inputs to the data target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonRedshiftTarget) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "data" in value:
        import aws_sdk_glue.types.amazon_redshift_node_data

        out["Data"] = (
            aws_sdk_glue.types.amazon_redshift_node_data.serialize_aws_json_1_1(
                value["data"]
            )
        )
    if "inputs" in value:
        import aws_sdk_glue.types.one_input

        out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(
            value["inputs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonRedshiftTarget:
    out: AmazonRedshiftTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Data" in data:
        import aws_sdk_glue.types.amazon_redshift_node_data

        out["data"] = (
            aws_sdk_glue.types.amazon_redshift_node_data.deserialize_aws_json_1_1(
                data["Data"]
            )
        )
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    return out
