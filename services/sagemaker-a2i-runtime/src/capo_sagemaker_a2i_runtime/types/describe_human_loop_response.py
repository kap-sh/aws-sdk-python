"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#DescribeHumanLoopResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_a2i_runtime.types.flow_definition_arn
    import capo_sagemaker_a2i_runtime.types.human_loop_arn
    import capo_sagemaker_a2i_runtime.types.human_loop_name
    import capo_sagemaker_a2i_runtime.types.human_loop_output
    import capo_sagemaker_a2i_runtime.types.human_loop_status
    import capo_sagemaker_a2i_runtime.types.string
    import capo_sagemaker_a2i_runtime.types.timestamp


class DescribeHumanLoopResponse(TypedDict, closed=True):
    creation_time: NotRequired["capo_sagemaker_a2i_runtime.types.timestamp.Timestamp"]
    """<p>The creation time when Amazon Augmented AI created the human loop.</p>"""
    failure_reason: NotRequired["capo_sagemaker_a2i_runtime.types.string.String"]
    """<p>The reason why a human loop failed. The failure reason is returned when the status of the human loop is <code>Failed</code>.</p>"""
    failure_code: NotRequired["capo_sagemaker_a2i_runtime.types.string.String"]
    """<p>A failure code that identifies the type of failure.</p> <p>Possible values: <code>ValidationError</code>, <code>Expired</code>, <code>InternalError</code> </p>"""
    human_loop_status: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_status.HumanLoopStatus"
    ]
    """<p>The status of the human loop. </p>"""
    human_loop_name: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
    ]
    """<p>The name of the human loop. The name must be lowercase, unique within the Region in your account, and can have up to 63 characters. Valid characters: a-z, 0-9, and - (hyphen).</p>"""
    human_loop_arn: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_arn.HumanLoopArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the human loop.</p>"""
    flow_definition_arn: NotRequired[
        "capo_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow definition.</p>"""
    human_loop_output: NotRequired[
        "capo_sagemaker_a2i_runtime.types.human_loop_output.HumanLoopOutput"
    ]
    """<p>An object that contains information about the output of the human loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHumanLoopResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_sagemaker_a2i_runtime.types.timestamp

        out["CreationTime"] = capo_sagemaker_a2i_runtime.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "failure_code" in value:
        out["FailureCode"] = value["failure_code"]
    if "human_loop_status" in value:
        import capo_sagemaker_a2i_runtime.types.human_loop_status

        out["HumanLoopStatus"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_status.serialize_json(
                value["human_loop_status"]
            )
        )
    if "human_loop_name" in value:
        out["HumanLoopName"] = value["human_loop_name"]
    if "human_loop_arn" in value:
        out["HumanLoopArn"] = value["human_loop_arn"]
    if "flow_definition_arn" in value:
        out["FlowDefinitionArn"] = value["flow_definition_arn"]
    if "human_loop_output" in value:
        import capo_sagemaker_a2i_runtime.types.human_loop_output

        out["HumanLoopOutput"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_output.serialize_json(
                value["human_loop_output"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeHumanLoopResponse:
    out: DescribeHumanLoopResponse = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import capo_sagemaker_a2i_runtime.types.timestamp

        out["creation_time"] = (
            capo_sagemaker_a2i_runtime.types.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "FailureCode" in data:
        out["failure_code"] = data["FailureCode"]
    if "HumanLoopStatus" in data:
        import capo_sagemaker_a2i_runtime.types.human_loop_status

        out["human_loop_status"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_status.deserialize_json(
                data["HumanLoopStatus"]
            )
        )
    if "HumanLoopName" in data:
        out["human_loop_name"] = data["HumanLoopName"]
    if "HumanLoopArn" in data:
        out["human_loop_arn"] = data["HumanLoopArn"]
    if "FlowDefinitionArn" in data:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    if "HumanLoopOutput" in data:
        import capo_sagemaker_a2i_runtime.types.human_loop_output

        out["human_loop_output"] = (
            capo_sagemaker_a2i_runtime.types.human_loop_output.deserialize_json(
                data["HumanLoopOutput"]
            )
        )
    return out
