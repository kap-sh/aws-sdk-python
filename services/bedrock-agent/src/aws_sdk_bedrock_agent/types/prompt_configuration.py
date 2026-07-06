"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.base_prompt_template
    import aws_sdk_bedrock_agent.types.creation_mode
    import aws_sdk_bedrock_agent.types.inference_configuration
    import aws_sdk_bedrock_agent.types.model_identifier
    import aws_sdk_bedrock_agent.types.prompt_state
    import aws_sdk_bedrock_agent.types.prompt_type


class PromptConfiguration(TypedDict, closed=True):
    prompt_type: NotRequired["aws_sdk_bedrock_agent.types.prompt_type.PromptType"]
    """<p>The step in the agent sequence that this prompt configuration applies to.</p>"""
    prompt_creation_mode: NotRequired[
        "aws_sdk_bedrock_agent.types.creation_mode.CreationMode"
    ]
    """<p>Specifies whether to override the default prompt template for this <code>promptType</code>. Set this value to <code>OVERRIDDEN</code> to use the prompt that you provide in the <code>basePromptTemplate</code>. If you leave it as <code>DEFAULT</code>, the agent uses a default prompt template.</p>"""
    prompt_state: NotRequired["aws_sdk_bedrock_agent.types.prompt_state.PromptState"]
    """<p>Specifies whether to allow the agent to carry out the step specified in the <code>promptType</code>. If you set this value to <code>DISABLED</code>, the agent skips that step. The default state for each <code>promptType</code> is as follows.</p> <ul> <li> <p> <code>PRE_PROCESSING</code> – <code>DISABLED</code> </p> </li> <li> <p> <code>ORCHESTRATION</code> – <code>ENABLED</code> </p> </li> <li> <p> <code>KNOWLEDGE_BASE_RESPONSE_GENERATION</code> – <code>ENABLED</code> </p> </li> <li> <p> <code>POST_PROCESSING</code> – <code>DISABLED</code> </p> </li> </ul>"""
    base_prompt_template: NotRequired[
        "aws_sdk_bedrock_agent.types.base_prompt_template.BasePromptTemplate"
    ]
    r"""<p>Defines the prompt template with which to replace the default prompt template. You can use placeholder variables in the base prompt template to customize the prompt. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html\">Prompt template placeholder variables</a>. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-configure.html\">Configure the prompt templates</a>.</p>"""
    inference_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.inference_configuration.InferenceConfiguration"
    ]
    r"""<p>Contains inference parameters to use when the agent invokes a foundation model in the part of the agent sequence defined by the <code>promptType</code>. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html\">Inference parameters for foundation models</a>.</p>"""
    parser_mode: NotRequired["aws_sdk_bedrock_agent.types.creation_mode.CreationMode"]
    r"""<p>Specifies whether to override the default parser Lambda function when parsing the raw foundation model output in the part of the agent sequence defined by the <code>promptType</code>. If you set the field as <code>OVERRIDDEN</code>, the <code>overrideLambda</code> field in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html\">PromptOverrideConfiguration</a> must be specified with the ARN of a Lambda function.</p>"""
    foundation_model: NotRequired[
        "aws_sdk_bedrock_agent.types.model_identifier.ModelIdentifier"
    ]
    """<p>The agent's foundation model.</p>"""
    additional_model_request_fields: NotRequired["object"]
    """<p>If the Converse or ConverseStream operations support the model, <code>additionalModelRequestFields</code> contains additional inference parameters, beyond the base set of inference parameters in the <code>inferenceConfiguration</code> field. </p> <p>For more information, see <i>Inference request parameters and response fields for foundation models</i> in the Amazon Bedrock user guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptConfiguration) -> dict:
    out: dict = {}
    if "prompt_type" in value:
        import aws_sdk_bedrock_agent.types.prompt_type

        out["promptType"] = aws_sdk_bedrock_agent.types.prompt_type.serialize_json(
            value["prompt_type"]
        )
    if "prompt_creation_mode" in value:
        import aws_sdk_bedrock_agent.types.creation_mode

        out["promptCreationMode"] = (
            aws_sdk_bedrock_agent.types.creation_mode.serialize_json(
                value["prompt_creation_mode"]
            )
        )
    if "prompt_state" in value:
        import aws_sdk_bedrock_agent.types.prompt_state

        out["promptState"] = aws_sdk_bedrock_agent.types.prompt_state.serialize_json(
            value["prompt_state"]
        )
    if "base_prompt_template" in value:
        out["basePromptTemplate"] = value["base_prompt_template"]
    if "inference_configuration" in value:
        import aws_sdk_bedrock_agent.types.inference_configuration

        out["inferenceConfiguration"] = (
            aws_sdk_bedrock_agent.types.inference_configuration.serialize_json(
                value["inference_configuration"]
            )
        )
    if "parser_mode" in value:
        import aws_sdk_bedrock_agent.types.creation_mode

        out["parserMode"] = aws_sdk_bedrock_agent.types.creation_mode.serialize_json(
            value["parser_mode"]
        )
    if "foundation_model" in value:
        out["foundationModel"] = value["foundation_model"]
    if "additional_model_request_fields" in value:
        out["additionalModelRequestFields"] = value["additional_model_request_fields"]
    return out


def deserialize_json(data: dict) -> PromptConfiguration:
    out: PromptConfiguration = {}  # type: ignore[typeddict-item]
    if "promptType" in data:
        import aws_sdk_bedrock_agent.types.prompt_type

        out["prompt_type"] = aws_sdk_bedrock_agent.types.prompt_type.deserialize_json(
            data["promptType"]
        )
    if "promptCreationMode" in data:
        import aws_sdk_bedrock_agent.types.creation_mode

        out["prompt_creation_mode"] = (
            aws_sdk_bedrock_agent.types.creation_mode.deserialize_json(
                data["promptCreationMode"]
            )
        )
    if "promptState" in data:
        import aws_sdk_bedrock_agent.types.prompt_state

        out["prompt_state"] = aws_sdk_bedrock_agent.types.prompt_state.deserialize_json(
            data["promptState"]
        )
    if "basePromptTemplate" in data:
        out["base_prompt_template"] = data["basePromptTemplate"]
    if "inferenceConfiguration" in data:
        import aws_sdk_bedrock_agent.types.inference_configuration

        out["inference_configuration"] = (
            aws_sdk_bedrock_agent.types.inference_configuration.deserialize_json(
                data["inferenceConfiguration"]
            )
        )
    if "parserMode" in data:
        import aws_sdk_bedrock_agent.types.creation_mode

        out["parser_mode"] = aws_sdk_bedrock_agent.types.creation_mode.deserialize_json(
            data["parserMode"]
        )
    if "foundationModel" in data:
        out["foundation_model"] = data["foundationModel"]
    if "additionalModelRequestFields" in data:
        out["additional_model_request_fields"] = data["additionalModelRequestFields"]
    return out
