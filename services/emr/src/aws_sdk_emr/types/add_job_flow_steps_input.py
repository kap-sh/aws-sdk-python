"""Generated from Smithy shape ``com.amazonaws.emr#AddJobFlowStepsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.step_config_list
    import aws_sdk_emr.types.xml_string_max_len256


class AddJobFlowStepsInput(TypedDict):
    job_flow_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>A string that uniquely identifies the job flow. This identifier is returned by <a>RunJobFlow</a> and can also be obtained from <a>ListClusters</a>. </p>"""
    steps: NotRequired["aws_sdk_emr.types.step_config_list.StepConfigList"]
    """<p> A list of <a>StepConfig</a> to be executed by the job flow. </p>"""
    execution_role_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the runtime role for a step on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: <code>arn:partition:service:region:account:resource</code>. </p> <p>For example, <code>arn:aws:IAM::1234567890:role/ReadOnly</code> is a correctly formatted runtime role ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddJobFlowStepsInput) -> dict:
    out: dict = {}
    if "job_flow_id" in value:
        out["JobFlowId"] = value["job_flow_id"]
    if "steps" in value:
        import aws_sdk_emr.types.step_config_list

        out["Steps"] = aws_sdk_emr.types.step_config_list.serialize_aws_json_1_1(
            value["steps"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddJobFlowStepsInput:
    out: AddJobFlowStepsInput = {}  # type: ignore[typeddict-item]
    if "JobFlowId" in data:
        out["job_flow_id"] = data["JobFlowId"]
    if "Steps" in data:
        import aws_sdk_emr.types.step_config_list

        out["steps"] = aws_sdk_emr.types.step_config_list.deserialize_aws_json_1_1(
            data["Steps"]
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    return out
