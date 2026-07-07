"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.error_message
    import aws_sdk_codedeploy.types.instance_summary_list


class BatchGetDeploymentInstancesOutput(TypedDict, closed=True):
    instances_summary: NotRequired[
        "aws_sdk_codedeploy.types.instance_summary_list.InstanceSummaryList"
    ]
    """<p>Information about the instance.</p>"""
    error_message: NotRequired["aws_sdk_codedeploy.types.error_message.ErrorMessage"]
    """<p>Information about errors that might have occurred during the API call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentInstancesOutput) -> dict:
    out: dict = {}
    if "instances_summary" in value:
        import aws_sdk_codedeploy.types.instance_summary_list

        out["instancesSummary"] = (
            aws_sdk_codedeploy.types.instance_summary_list.serialize_aws_json_1_1(
                value["instances_summary"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentInstancesOutput:
    out: BatchGetDeploymentInstancesOutput = {}  # type: ignore[typeddict-item]
    if "instancesSummary" in data:
        import aws_sdk_codedeploy.types.instance_summary_list

        out["instances_summary"] = (
            aws_sdk_codedeploy.types.instance_summary_list.deserialize_aws_json_1_1(
                data["instancesSummary"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
