"""Generated from Smithy shape ``com.amazonaws.emr#SetUnhealthyNodeReplacementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.xml_string_list


class SetUnhealthyNodeReplacementInput(TypedDict, closed=True):
    job_flow_ids: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p>The list of strings that uniquely identify the clusters for which to turn on unhealthy node replacement. You can get these identifiers by running the <a>RunJobFlow</a> or the <a>DescribeJobFlows</a> operations.</p>"""
    unhealthy_node_replacement: NotRequired[
        "aws_sdk_emr.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether to turn on or turn off graceful unhealthy node replacement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUnhealthyNodeReplacementInput) -> dict:
    out: dict = {}
    if "job_flow_ids" in value:
        import aws_sdk_emr.types.xml_string_list

        out["JobFlowIds"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    if "unhealthy_node_replacement" in value:
        out["UnhealthyNodeReplacement"] = value["unhealthy_node_replacement"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUnhealthyNodeReplacementInput:
    out: SetUnhealthyNodeReplacementInput = {}  # type: ignore[typeddict-item]
    if "JobFlowIds" in data:
        import aws_sdk_emr.types.xml_string_list

        out["job_flow_ids"] = (
            aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
                data["JobFlowIds"]
            )
        )
    if "UnhealthyNodeReplacement" in data:
        out["unhealthy_node_replacement"] = data["UnhealthyNodeReplacement"]
    return out
