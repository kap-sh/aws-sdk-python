"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDataQualityJobDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_job_definition_name


class DescribeDataQualityJobDefinitionRequest(TypedDict, closed=True):
    job_definition_name: NotRequired[
        "capo_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the data quality monitoring job definition to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataQualityJobDefinitionRequest) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataQualityJobDefinitionRequest:
    out: DescribeDataQualityJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "JobDefinitionName" in data:
        out["job_definition_name"] = data["JobDefinitionName"]
    return out
