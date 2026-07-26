"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateFlowDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.flow_definition_name
    import capo_sagemaker.types.flow_definition_output_config
    import capo_sagemaker.types.human_loop_activation_config
    import capo_sagemaker.types.human_loop_config
    import capo_sagemaker.types.human_loop_request_source
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreateFlowDefinitionRequest(TypedDict, closed=True):
    flow_definition_name: NotRequired[
        "capo_sagemaker.types.flow_definition_name.FlowDefinitionName"
    ]
    """<p>The name of your flow definition.</p>"""
    human_loop_request_source: NotRequired[
        "capo_sagemaker.types.human_loop_request_source.HumanLoopRequestSource"
    ]
    """<p>Container for configuring the source of human task requests. Use to specify if Amazon Rekognition or Amazon Textract is used as an integration source.</p>"""
    human_loop_activation_config: NotRequired[
        "capo_sagemaker.types.human_loop_activation_config.HumanLoopActivationConfig"
    ]
    """<p>An object containing information about the events that trigger a human workflow.</p>"""
    human_loop_config: NotRequired[
        "capo_sagemaker.types.human_loop_config.HumanLoopConfig"
    ]
    """<p>An object containing information about the tasks the human reviewers will perform.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.flow_definition_output_config.FlowDefinitionOutputConfig"
    ]
    """<p>An object containing information about where the human review results will be uploaded.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role needed to call other services on your behalf. For example, <code>arn:aws:iam::1234567890:role/service-role/AmazonSageMaker-ExecutionRole-20180111T151298</code>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>An array of key-value pairs that contain metadata to help you categorize and organize a flow definition. Each tag consists of a key and a value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFlowDefinitionRequest) -> dict:
    out: dict = {}
    if "flow_definition_name" in value:
        out["FlowDefinitionName"] = value["flow_definition_name"]
    if "human_loop_request_source" in value:
        import capo_sagemaker.types.human_loop_request_source

        out["HumanLoopRequestSource"] = (
            capo_sagemaker.types.human_loop_request_source.serialize_aws_json_1_1(
                value["human_loop_request_source"]
            )
        )
    if "human_loop_activation_config" in value:
        import capo_sagemaker.types.human_loop_activation_config

        out["HumanLoopActivationConfig"] = (
            capo_sagemaker.types.human_loop_activation_config.serialize_aws_json_1_1(
                value["human_loop_activation_config"]
            )
        )
    if "human_loop_config" in value:
        import capo_sagemaker.types.human_loop_config

        out["HumanLoopConfig"] = (
            capo_sagemaker.types.human_loop_config.serialize_aws_json_1_1(
                value["human_loop_config"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.flow_definition_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.flow_definition_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFlowDefinitionRequest:
    out: CreateFlowDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "FlowDefinitionName" in data:
        out["flow_definition_name"] = data["FlowDefinitionName"]
    if "HumanLoopRequestSource" in data:
        import capo_sagemaker.types.human_loop_request_source

        out["human_loop_request_source"] = (
            capo_sagemaker.types.human_loop_request_source.deserialize_aws_json_1_1(
                data["HumanLoopRequestSource"]
            )
        )
    if "HumanLoopActivationConfig" in data:
        import capo_sagemaker.types.human_loop_activation_config

        out["human_loop_activation_config"] = (
            capo_sagemaker.types.human_loop_activation_config.deserialize_aws_json_1_1(
                data["HumanLoopActivationConfig"]
            )
        )
    if "HumanLoopConfig" in data:
        import capo_sagemaker.types.human_loop_config

        out["human_loop_config"] = (
            capo_sagemaker.types.human_loop_config.deserialize_aws_json_1_1(
                data["HumanLoopConfig"]
            )
        )
    if "OutputConfig" in data:
        import capo_sagemaker.types.flow_definition_output_config

        out["output_config"] = (
            capo_sagemaker.types.flow_definition_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
