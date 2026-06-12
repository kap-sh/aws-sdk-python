"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.failure_reason
    import aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_name
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_status
    import aws_sdk_sagemaker_a2i_runtime.types.timestamp


class HumanLoopSummary(TypedDict):
    human_loop_name: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
    ]
    """<p>The name of the human loop.</p>"""
    human_loop_status: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.human_loop_status.HumanLoopStatus"
    ]
    """<p>The status of the human loop. </p>"""
    creation_time: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.timestamp.Timestamp"
    ]
    """<p>When Amazon Augmented AI created the human loop.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.failure_reason.FailureReason"
    ]
    """<p>The reason why the human loop failed. A failure reason is returned when the status of the human loop is <code>Failed</code>.</p>"""
    flow_definition_arn: NotRequired[
        "aws_sdk_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow definition used to configure the human loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanLoopSummary) -> dict:
    out: dict = {}
    if "human_loop_name" in value:
        out["HumanLoopName"] = value["human_loop_name"]
    if "human_loop_status" in value:
        import aws_sdk_sagemaker_a2i_runtime.types.human_loop_status

        out["HumanLoopStatus"] = (
            aws_sdk_sagemaker_a2i_runtime.types.human_loop_status.serialize_json(
                value["human_loop_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker_a2i_runtime.types.timestamp

        out["CreationTime"] = (
            aws_sdk_sagemaker_a2i_runtime.types.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "flow_definition_arn" in value:
        out["FlowDefinitionArn"] = value["flow_definition_arn"]
    return out


def deserialize_json(data: dict) -> HumanLoopSummary:
    out: HumanLoopSummary = {}  # type: ignore[typeddict-item]
    if "HumanLoopName" in data:
        out["human_loop_name"] = data["HumanLoopName"]
    if "HumanLoopStatus" in data:
        import aws_sdk_sagemaker_a2i_runtime.types.human_loop_status

        out["human_loop_status"] = (
            aws_sdk_sagemaker_a2i_runtime.types.human_loop_status.deserialize_json(
                data["HumanLoopStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker_a2i_runtime.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker_a2i_runtime.types.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "FlowDefinitionArn" in data:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    return out
