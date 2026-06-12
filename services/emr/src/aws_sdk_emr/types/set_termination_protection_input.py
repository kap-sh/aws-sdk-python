"""Generated from Smithy shape ``com.amazonaws.emr#SetTerminationProtectionInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.xml_string_list


class SetTerminationProtectionInput(TypedDict):
    job_flow_ids: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p> A list of strings that uniquely identify the clusters to protect. This identifier is returned by <a>RunJobFlow</a> and can also be obtained from <a>DescribeJobFlows</a> . </p>"""
    termination_protected: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>A Boolean that indicates whether to protect the cluster and prevent the Amazon EC2 instances in the cluster from shutting down due to API calls, user intervention, or job-flow error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetTerminationProtectionInput) -> dict:
    out: dict = {}
    if "job_flow_ids" in value:
        import aws_sdk_emr.types.xml_string_list

        out["JobFlowIds"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    if "termination_protected" in value:
        out["TerminationProtected"] = value["termination_protected"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetTerminationProtectionInput:
    out: SetTerminationProtectionInput = {}  # type: ignore[typeddict-item]
    if "JobFlowIds" in data:
        import aws_sdk_emr.types.xml_string_list

        out["job_flow_ids"] = (
            aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
                data["JobFlowIds"]
            )
        )
    if "TerminationProtected" in data:
        out["termination_protected"] = data["TerminationProtected"]
    return out
