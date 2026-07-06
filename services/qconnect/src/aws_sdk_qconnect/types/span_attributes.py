"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_type
    import aws_sdk_qconnect.types.ai_prompt_type
    import aws_sdk_qconnect.types.arn_with_qualifier
    import aws_sdk_qconnect.types.generic_arn
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.span_finish_reason_list
    import aws_sdk_qconnect.types.span_guardrail_assessment_list
    import aws_sdk_qconnect.types.span_message_list
    import aws_sdk_qconnect.types.span_message_value_list
    import aws_sdk_qconnect.types.uuid


class SpanAttributes(TypedDict, closed=True):
    operation_name: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>Action being performed</p>"""
    provider_name: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>Model provider identifier (e.g., aws.bedrock)</p>"""
    error_type: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>Error classification if span failed (e.g., throttle, timeout)</p>"""
    agent_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>Amazon Connect agent ID</p>"""
    instance_arn: NotRequired["aws_sdk_qconnect.types.generic_arn.GenericArn"]
    """<p>Amazon Connect instance ARN</p>"""
    contact_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>Amazon Connect contact identifier</p>"""
    initial_contact_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>Amazon Connect contact identifier</p>"""
    session_name: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>Session name</p>"""
    ai_agent_arn: NotRequired[
        "aws_sdk_qconnect.types.arn_with_qualifier.ArnWithQualifier"
    ]
    """<p>AI agent ARN</p>"""
    ai_agent_type: NotRequired["aws_sdk_qconnect.types.ai_agent_type.AIAgentType"]
    """<p>AI agent type</p>"""
    ai_agent_name: NotRequired["aws_sdk_qconnect.types.name.Name"]
    """<p>AI agent name</p>"""
    ai_agent_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>AI agent identifier</p>"""
    ai_agent_version: NotRequired["int"]
    """<p>AI agent version number</p>"""
    ai_agent_invoker: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>Entity that invoked the AI agent</p>"""
    ai_agent_orchestrator_use_case: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>AI agent orchestrator use case</p>"""
    request_model: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>LLM model ID for request (e.g., anthropic.claude-3-sonnet)</p>"""
    request_max_tokens: NotRequired["int"]
    """<p>Maximum tokens configured for generation</p>"""
    temperature: NotRequired["float"]
    """<p>Sampling temperature for generation</p>"""
    top_p: NotRequired["float"]
    """<p>Top-p sampling parameter for generation</p>"""
    response_model: NotRequired[
        "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    ]
    """<p>Actual model used for response (usually matches requestModel)</p>"""
    response_finish_reasons: NotRequired[
        "aws_sdk_qconnect.types.span_finish_reason_list.SpanFinishReasonList"
    ]
    """<p>Generation termination reasons (e.g., stop, max_tokens)</p>"""
    usage_input_tokens: NotRequired["int"]
    """<p>Number of input tokens in prompt</p>"""
    usage_output_tokens: NotRequired["int"]
    """<p>Number of output tokens in response</p>"""
    usage_total_tokens: NotRequired["int"]
    """<p>Total tokens consumed (input + output)</p>"""
    cache_read_input_tokens: NotRequired["int"]
    """<p>Number of input tokens that were retrieved from cache</p>"""
    cache_write_input_tokens: NotRequired["int"]
    """<p>Number of input tokens that were written to cache in this request</p>"""
    input_messages: NotRequired[
        "aws_sdk_qconnect.types.span_message_list.SpanMessageList"
    ]
    """<p>Input message collection sent to LLM</p>"""
    output_messages: NotRequired[
        "aws_sdk_qconnect.types.span_message_list.SpanMessageList"
    ]
    """<p>Output message collection received from LLM</p>"""
    system_instructions: NotRequired[
        "aws_sdk_qconnect.types.span_message_value_list.SpanMessageValueList"
    ]
    """<p>System prompt instructions</p>"""
    prompt_arn: NotRequired[
        "aws_sdk_qconnect.types.arn_with_qualifier.ArnWithQualifier"
    ]
    """<p>AI prompt ARN</p>"""
    prompt_id: NotRequired["aws_sdk_qconnect.types.uuid.Uuid"]
    """<p>AI prompt identifier</p>"""
    prompt_type: NotRequired["aws_sdk_qconnect.types.ai_prompt_type.AIPromptType"]
    """<p>AI prompt type</p>"""
    prompt_name: NotRequired["aws_sdk_qconnect.types.name.Name"]
    """<p>AI prompt name</p>"""
    prompt_version: NotRequired["int"]
    """<p>AI prompt version number</p>"""
    time_to_first_token_ms: NotRequired["int"]
    """<p>Time to first token in milliseconds, measured from when Amazon Bedrock was invoked to when the first token was returned</p>"""
    guardrail_assessments: NotRequired[
        "aws_sdk_qconnect.types.span_guardrail_assessment_list.SpanGuardrailAssessmentList"
    ]
    """<p>Guardrail assessments for the inference span. Absent on other span types and when no AI Guardrail is attached to the AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanAttributes) -> dict:
    out: dict = {}
    if "operation_name" in value:
        out["operationName"] = value["operation_name"]
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "contact_id" in value:
        out["contactId"] = value["contact_id"]
    if "initial_contact_id" in value:
        out["initialContactId"] = value["initial_contact_id"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "ai_agent_arn" in value:
        out["aiAgentArn"] = value["ai_agent_arn"]
    if "ai_agent_type" in value:
        out["aiAgentType"] = value["ai_agent_type"]
    if "ai_agent_name" in value:
        out["aiAgentName"] = value["ai_agent_name"]
    if "ai_agent_id" in value:
        out["aiAgentId"] = value["ai_agent_id"]
    if "ai_agent_version" in value:
        out["aiAgentVersion"] = value["ai_agent_version"]
    if "ai_agent_invoker" in value:
        out["aiAgentInvoker"] = value["ai_agent_invoker"]
    if "ai_agent_orchestrator_use_case" in value:
        out["aiAgentOrchestratorUseCase"] = value["ai_agent_orchestrator_use_case"]
    if "request_model" in value:
        out["requestModel"] = value["request_model"]
    if "request_max_tokens" in value:
        out["requestMaxTokens"] = value["request_max_tokens"]
    if "temperature" in value:
        out["temperature"] = value["temperature"]
    if "top_p" in value:
        out["topP"] = value["top_p"]
    if "response_model" in value:
        out["responseModel"] = value["response_model"]
    if "response_finish_reasons" in value:
        import aws_sdk_qconnect.types.span_finish_reason_list

        out["responseFinishReasons"] = (
            aws_sdk_qconnect.types.span_finish_reason_list.serialize_json(
                value["response_finish_reasons"]
            )
        )
    if "usage_input_tokens" in value:
        out["usageInputTokens"] = value["usage_input_tokens"]
    if "usage_output_tokens" in value:
        out["usageOutputTokens"] = value["usage_output_tokens"]
    if "usage_total_tokens" in value:
        out["usageTotalTokens"] = value["usage_total_tokens"]
    if "cache_read_input_tokens" in value:
        out["cacheReadInputTokens"] = value["cache_read_input_tokens"]
    if "cache_write_input_tokens" in value:
        out["cacheWriteInputTokens"] = value["cache_write_input_tokens"]
    if "input_messages" in value:
        import aws_sdk_qconnect.types.span_message_list

        out["inputMessages"] = aws_sdk_qconnect.types.span_message_list.serialize_json(
            value["input_messages"]
        )
    if "output_messages" in value:
        import aws_sdk_qconnect.types.span_message_list

        out["outputMessages"] = aws_sdk_qconnect.types.span_message_list.serialize_json(
            value["output_messages"]
        )
    if "system_instructions" in value:
        import aws_sdk_qconnect.types.span_message_value_list

        out["systemInstructions"] = (
            aws_sdk_qconnect.types.span_message_value_list.serialize_json(
                value["system_instructions"]
            )
        )
    if "prompt_arn" in value:
        out["promptArn"] = value["prompt_arn"]
    if "prompt_id" in value:
        out["promptId"] = value["prompt_id"]
    if "prompt_type" in value:
        out["promptType"] = value["prompt_type"]
    if "prompt_name" in value:
        out["promptName"] = value["prompt_name"]
    if "prompt_version" in value:
        out["promptVersion"] = value["prompt_version"]
    if "time_to_first_token_ms" in value:
        out["timeToFirstTokenMs"] = value["time_to_first_token_ms"]
    if "guardrail_assessments" in value:
        import aws_sdk_qconnect.types.span_guardrail_assessment_list

        out["guardrailAssessments"] = (
            aws_sdk_qconnect.types.span_guardrail_assessment_list.serialize_json(
                value["guardrail_assessments"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpanAttributes:
    out: SpanAttributes = {}  # type: ignore[typeddict-item]
    if "operationName" in data:
        out["operation_name"] = data["operationName"]
    if "providerName" in data:
        out["provider_name"] = data["providerName"]
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    if "contactId" in data:
        out["contact_id"] = data["contactId"]
    if "initialContactId" in data:
        out["initial_contact_id"] = data["initialContactId"]
    if "sessionName" in data:
        out["session_name"] = data["sessionName"]
    if "aiAgentArn" in data:
        out["ai_agent_arn"] = data["aiAgentArn"]
    if "aiAgentType" in data:
        out["ai_agent_type"] = data["aiAgentType"]
    if "aiAgentName" in data:
        out["ai_agent_name"] = data["aiAgentName"]
    if "aiAgentId" in data:
        out["ai_agent_id"] = data["aiAgentId"]
    if "aiAgentVersion" in data:
        out["ai_agent_version"] = data["aiAgentVersion"]
    if "aiAgentInvoker" in data:
        out["ai_agent_invoker"] = data["aiAgentInvoker"]
    if "aiAgentOrchestratorUseCase" in data:
        out["ai_agent_orchestrator_use_case"] = data["aiAgentOrchestratorUseCase"]
    if "requestModel" in data:
        out["request_model"] = data["requestModel"]
    if "requestMaxTokens" in data:
        out["request_max_tokens"] = data["requestMaxTokens"]
    if "temperature" in data:
        out["temperature"] = data["temperature"]
    if "topP" in data:
        out["top_p"] = data["topP"]
    if "responseModel" in data:
        out["response_model"] = data["responseModel"]
    if "responseFinishReasons" in data:
        import aws_sdk_qconnect.types.span_finish_reason_list

        out["response_finish_reasons"] = (
            aws_sdk_qconnect.types.span_finish_reason_list.deserialize_json(
                data["responseFinishReasons"]
            )
        )
    if "usageInputTokens" in data:
        out["usage_input_tokens"] = data["usageInputTokens"]
    if "usageOutputTokens" in data:
        out["usage_output_tokens"] = data["usageOutputTokens"]
    if "usageTotalTokens" in data:
        out["usage_total_tokens"] = data["usageTotalTokens"]
    if "cacheReadInputTokens" in data:
        out["cache_read_input_tokens"] = data["cacheReadInputTokens"]
    if "cacheWriteInputTokens" in data:
        out["cache_write_input_tokens"] = data["cacheWriteInputTokens"]
    if "inputMessages" in data:
        import aws_sdk_qconnect.types.span_message_list

        out["input_messages"] = (
            aws_sdk_qconnect.types.span_message_list.deserialize_json(
                data["inputMessages"]
            )
        )
    if "outputMessages" in data:
        import aws_sdk_qconnect.types.span_message_list

        out["output_messages"] = (
            aws_sdk_qconnect.types.span_message_list.deserialize_json(
                data["outputMessages"]
            )
        )
    if "systemInstructions" in data:
        import aws_sdk_qconnect.types.span_message_value_list

        out["system_instructions"] = (
            aws_sdk_qconnect.types.span_message_value_list.deserialize_json(
                data["systemInstructions"]
            )
        )
    if "promptArn" in data:
        out["prompt_arn"] = data["promptArn"]
    if "promptId" in data:
        out["prompt_id"] = data["promptId"]
    if "promptType" in data:
        out["prompt_type"] = data["promptType"]
    if "promptName" in data:
        out["prompt_name"] = data["promptName"]
    if "promptVersion" in data:
        out["prompt_version"] = data["promptVersion"]
    if "timeToFirstTokenMs" in data:
        out["time_to_first_token_ms"] = data["timeToFirstTokenMs"]
    if "guardrailAssessments" in data:
        import aws_sdk_qconnect.types.span_guardrail_assessment_list

        out["guardrail_assessments"] = (
            aws_sdk_qconnect.types.span_guardrail_assessment_list.deserialize_json(
                data["guardrailAssessments"]
            )
        )
    return out
