"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelQualityJobDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_job_definition_arn


class CreateModelQualityJobDefinitionResponse(TypedDict, closed=True):
    job_definition_arn: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_arn.MonitoringJobDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model quality monitoring job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelQualityJobDefinitionResponse) -> dict:
    out: dict = {}
    if "job_definition_arn" in value:
        out["JobDefinitionArn"] = value["job_definition_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelQualityJobDefinitionResponse:
    out: CreateModelQualityJobDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "JobDefinitionArn" in data:
        out["job_definition_arn"] = data["JobDefinitionArn"]
    return out
