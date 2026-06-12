"""Generated from Smithy shape ``com.amazonaws.glue#AmazonRedshiftSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.amazon_redshift_node_data
    import aws_sdk_glue.types.node_name


class AmazonRedshiftSource(TypedDict):
    name: NotRequired["aws_sdk_glue.types.node_name.NodeName"]
    """<p>The name of the Amazon Redshift source.</p>"""
    data: NotRequired[
        "aws_sdk_glue.types.amazon_redshift_node_data.AmazonRedshiftNodeData"
    ]
    """<p>Specifies the data of the Amazon Reshift source node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonRedshiftSource) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonRedshiftSource:
    out: AmazonRedshiftSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Data" in data:
        import aws_sdk_glue.types.amazon_redshift_node_data

        out["data"] = (
            aws_sdk_glue.types.amazon_redshift_node_data.deserialize_aws_json_1_1(
                data["Data"]
            )
        )
    return out
