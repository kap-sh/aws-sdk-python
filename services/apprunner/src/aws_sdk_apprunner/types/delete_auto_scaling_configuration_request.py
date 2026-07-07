"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteAutoScalingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.boolean


class DeleteAutoScalingConfigurationRequest(TypedDict, closed=True):
    auto_scaling_configuration_arn: (
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to delete.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is deleted.</p>"""
    delete_all_revisions: "aws_sdk_apprunner.types.boolean.Boolean"
    """<p>Set to <code>true</code> to delete all of the revisions associated with the <code>AutoScalingConfigurationArn</code> parameter value.</p> <p>When <code>DeleteAllRevisions</code> is set to <code>true</code>, the only valid value for the Amazon Resource Name (ARN) is a partial ARN ending with: <code>.../name</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutoScalingConfigurationRequest) -> dict:
    out: dict = {}
    out["AutoScalingConfigurationArn"] = value["auto_scaling_configuration_arn"]
    out["DeleteAllRevisions"] = value.get("delete_all_revisions", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutoScalingConfigurationRequest:
    out: DeleteAutoScalingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfigurationArn" in data:
        out["auto_scaling_configuration_arn"] = data["AutoScalingConfigurationArn"]
    else:
        raise DeserializationError(
            "DeleteAutoScalingConfigurationRequest.auto_scaling_configuration_arn required"
        )
    if "DeleteAllRevisions" in data:
        out["delete_all_revisions"] = data["DeleteAllRevisions"]
    else:
        out["delete_all_revisions"] = False
    return out
