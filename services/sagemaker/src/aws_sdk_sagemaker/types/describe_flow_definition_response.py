"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeFlowDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.flow_definition_arn
    import aws_sdk_sagemaker.types.flow_definition_name
    import aws_sdk_sagemaker.types.flow_definition_output_config
    import aws_sdk_sagemaker.types.flow_definition_status
    import aws_sdk_sagemaker.types.human_loop_activation_config
    import aws_sdk_sagemaker.types.human_loop_config
    import aws_sdk_sagemaker.types.human_loop_request_source
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class DescribeFlowDefinitionResponse(TypedDict):
    flow_definition_arn: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_arn.FlowDefinitionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow defintion.</p>"""
    flow_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_name.FlowDefinitionName"
    ]
    """<p>The Amazon Resource Name (ARN) of the flow definition.</p>"""
    flow_definition_status: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_status.FlowDefinitionStatus"
    ]
    """<p>The status of the flow definition. Valid values are listed below.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the flow definition was created.</p>"""
    human_loop_request_source: NotRequired[
        "aws_sdk_sagemaker.types.human_loop_request_source.HumanLoopRequestSource"
    ]
    """<p>Container for configuring the source of human task requests. Used to specify if Amazon Rekognition or Amazon Textract is used as an integration source.</p>"""
    human_loop_activation_config: NotRequired[
        "aws_sdk_sagemaker.types.human_loop_activation_config.HumanLoopActivationConfig"
    ]
    """<p>An object containing information about what triggers a human review workflow.</p>"""
    human_loop_config: NotRequired[
        "aws_sdk_sagemaker.types.human_loop_config.HumanLoopConfig"
    ]
    """<p>An object containing information about who works on the task, the workforce task price, and other task details.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.flow_definition_output_config.FlowDefinitionOutputConfig"
    ]
    """<p>An object containing information about the output file.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) execution role for the flow definition.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason your flow definition failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFlowDefinitionResponse) -> dict:
    out: dict = {}
    if "flow_definition_arn" in value:
        out["FlowDefinitionArn"] = value["flow_definition_arn"]
    if "flow_definition_name" in value:
        out["FlowDefinitionName"] = value["flow_definition_name"]
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
    if "human_loop_request_source" in value:
        import aws_sdk_sagemaker.types.human_loop_request_source

        out["HumanLoopRequestSource"] = (
            aws_sdk_sagemaker.types.human_loop_request_source.serialize_aws_json_1_1(
                value["human_loop_request_source"]
            )
        )
    if "human_loop_activation_config" in value:
        import aws_sdk_sagemaker.types.human_loop_activation_config

        out["HumanLoopActivationConfig"] = (
            aws_sdk_sagemaker.types.human_loop_activation_config.serialize_aws_json_1_1(
                value["human_loop_activation_config"]
            )
        )
    if "human_loop_config" in value:
        import aws_sdk_sagemaker.types.human_loop_config

        out["HumanLoopConfig"] = (
            aws_sdk_sagemaker.types.human_loop_config.serialize_aws_json_1_1(
                value["human_loop_config"]
            )
        )
    if "output_config" in value:
        import aws_sdk_sagemaker.types.flow_definition_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.flow_definition_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFlowDefinitionResponse:
    out: DescribeFlowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionArn" in data:
        out["flow_definition_arn"] = data["FlowDefinitionArn"]
    if "FlowDefinitionName" in data:
        out["flow_definition_name"] = data["FlowDefinitionName"]
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
    if "HumanLoopRequestSource" in data:
        import aws_sdk_sagemaker.types.human_loop_request_source

        out["human_loop_request_source"] = (
            aws_sdk_sagemaker.types.human_loop_request_source.deserialize_aws_json_1_1(
                data["HumanLoopRequestSource"]
            )
        )
    if "HumanLoopActivationConfig" in data:
        import aws_sdk_sagemaker.types.human_loop_activation_config

        out["human_loop_activation_config"] = (
            aws_sdk_sagemaker.types.human_loop_activation_config.deserialize_aws_json_1_1(
                data["HumanLoopActivationConfig"]
            )
        )
    if "HumanLoopConfig" in data:
        import aws_sdk_sagemaker.types.human_loop_config

        out["human_loop_config"] = (
            aws_sdk_sagemaker.types.human_loop_config.deserialize_aws_json_1_1(
                data["HumanLoopConfig"]
            )
        )
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.flow_definition_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.flow_definition_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
