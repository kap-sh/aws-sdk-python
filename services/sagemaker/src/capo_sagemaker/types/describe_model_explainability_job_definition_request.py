"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelExplainabilityJobDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_job_definition_name


class DescribeModelExplainabilityJobDefinitionRequest(TypedDict, closed=True):
    job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the model explainability job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeModelExplainabilityJobDefinitionRequest,
) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeModelExplainabilityJobDefinitionRequest:
    out: DescribeModelExplainabilityJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "JobDefinitionName" in data:
        out["job_definition_name"] = data["JobDefinitionName"]
    return out
