"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelExplainabilityJobDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_job_definition_arn


class CreateModelExplainabilityJobDefinitionResponse(TypedDict):
    job_definition_arn: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_arn.MonitoringJobDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model explainability job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateModelExplainabilityJobDefinitionResponse,
) -> dict:
    out: dict = {}
    if "job_definition_arn" in value:
        out["JobDefinitionArn"] = value["job_definition_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateModelExplainabilityJobDefinitionResponse:
    out: CreateModelExplainabilityJobDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "JobDefinitionArn" in data:
        out["job_definition_arn"] = data["JobDefinitionArn"]
    return out
