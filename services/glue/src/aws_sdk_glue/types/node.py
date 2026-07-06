"""Generated from Smithy shape ``com.amazonaws.glue#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_node_details
    import aws_sdk_glue.types.job_node_details
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.node_type
    import aws_sdk_glue.types.trigger_node_details


class Node(TypedDict, closed=True):
    type: NotRequired["aws_sdk_glue.types.node_type.NodeType"]
    """<p>The type of Glue component represented by the node.</p>"""
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the Glue component represented by the node.</p>"""
    unique_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The unique Id assigned to the node within the workflow.</p>"""
    trigger_details: NotRequired[
        "aws_sdk_glue.types.trigger_node_details.TriggerNodeDetails"
    ]
    """<p>Details of the Trigger when the node represents a Trigger.</p>"""
    job_details: NotRequired["aws_sdk_glue.types.job_node_details.JobNodeDetails"]
    """<p>Details of the Job when the node represents a Job.</p>"""
    crawler_details: NotRequired[
        "aws_sdk_glue.types.crawler_node_details.CrawlerNodeDetails"
    ]
    """<p>Details of the crawler when the node represents a crawler.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Node) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_glue.types.node_type

        out["Type"] = aws_sdk_glue.types.node_type.serialize_aws_json_1_1(value["type"])
    if "name" in value:
        out["Name"] = value["name"]
    if "unique_id" in value:
        out["UniqueId"] = value["unique_id"]
    if "trigger_details" in value:
        import aws_sdk_glue.types.trigger_node_details

        out["TriggerDetails"] = (
            aws_sdk_glue.types.trigger_node_details.serialize_aws_json_1_1(
                value["trigger_details"]
            )
        )
    if "job_details" in value:
        import aws_sdk_glue.types.job_node_details

        out["JobDetails"] = aws_sdk_glue.types.job_node_details.serialize_aws_json_1_1(
            value["job_details"]
        )
    if "crawler_details" in value:
        import aws_sdk_glue.types.crawler_node_details

        out["CrawlerDetails"] = (
            aws_sdk_glue.types.crawler_node_details.serialize_aws_json_1_1(
                value["crawler_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_glue.types.node_type

        out["type"] = aws_sdk_glue.types.node_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "UniqueId" in data:
        out["unique_id"] = data["UniqueId"]
    if "TriggerDetails" in data:
        import aws_sdk_glue.types.trigger_node_details

        out["trigger_details"] = (
            aws_sdk_glue.types.trigger_node_details.deserialize_aws_json_1_1(
                data["TriggerDetails"]
            )
        )
    if "JobDetails" in data:
        import aws_sdk_glue.types.job_node_details

        out["job_details"] = (
            aws_sdk_glue.types.job_node_details.deserialize_aws_json_1_1(
                data["JobDetails"]
            )
        )
    if "CrawlerDetails" in data:
        import aws_sdk_glue.types.crawler_node_details

        out["crawler_details"] = (
            aws_sdk_glue.types.crawler_node_details.deserialize_aws_json_1_1(
                data["CrawlerDetails"]
            )
        )
    return out
