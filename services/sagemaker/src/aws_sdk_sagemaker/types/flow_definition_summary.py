"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.flow_definition_arn
    import aws_sdk_sagemaker.types.flow_definition_name
    import aws_sdk_sagemaker.types.flow_definition_status
    import aws_sdk_sagemaker.types.timestamp


class FlowDefinitionSummary(TypedDict):
    flow_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_name.FlowDefinitionName"
    ]
    """<p>The name of the flow definition.</p>"""
    flow_definition_arn: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow definition.</p>"""
    flow_definition_status: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_status.FlowDefinitionStatus"
    ]
    """<p>The status of the flow definition. Valid values:</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when SageMaker created the flow definition.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason why the flow definition creation failed. A failure reason is returned only when the flow definition status is <code>Failed</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowDefinitionSummary) -> dict:
    out: dict = {}
    if "flow_definition_name" in value:
        out["FlowDefinitionName"] = value["flow_definition_name"]
    if "flow_definition_arn" in value:
        out["FlowDefinitionArn"] = value["flow_definition_arn"]
    if "flow_definition_status" in value:
        import aws_sdk_sagemaker.types.flow_definition_status

        out["FlowDefinitionStatus"] = (
            aws_sdk_sagemaker.types.flow_definition_status.serialize_aws_json_1_1(
                value["flow_definition_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowDefinitionSummary:
    out: FlowDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionName" in data:
        out["flow_definition_name"] = data["FlowDefinitionName"]
    if "FlowDefinitionArn" in data:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    if "FlowDefinitionStatus" in data:
        import aws_sdk_sagemaker.types.flow_definition_status

        out["flow_definition_status"] = (
            aws_sdk_sagemaker.types.flow_definition_status.deserialize_aws_json_1_1(
                data["FlowDefinitionStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
