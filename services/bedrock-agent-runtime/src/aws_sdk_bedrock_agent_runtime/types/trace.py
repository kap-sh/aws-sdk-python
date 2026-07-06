"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Trace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace
    import aws_sdk_bedrock_agent_runtime.types.failure_trace
    import aws_sdk_bedrock_agent_runtime.types.guardrail_trace
    import aws_sdk_bedrock_agent_runtime.types.orchestration_trace
    import aws_sdk_bedrock_agent_runtime.types.post_processing_trace
    import aws_sdk_bedrock_agent_runtime.types.pre_processing_trace
    import aws_sdk_bedrock_agent_runtime.types.routing_classifier_trace


class _Trace_guardrailTrace(TypedDict, closed=True):
    guardrailTrace: "aws_sdk_bedrock_agent_runtime.types.guardrail_trace.GuardrailTrace"


class _Trace_preProcessingTrace(TypedDict, closed=True):
    preProcessingTrace: (
        "aws_sdk_bedrock_agent_runtime.types.pre_processing_trace.PreProcessingTrace"
    )


class _Trace_orchestrationTrace(TypedDict, closed=True):
    orchestrationTrace: (
        "aws_sdk_bedrock_agent_runtime.types.orchestration_trace.OrchestrationTrace"
    )


class _Trace_postProcessingTrace(TypedDict, closed=True):
    postProcessingTrace: (
        "aws_sdk_bedrock_agent_runtime.types.post_processing_trace.PostProcessingTrace"
    )


class _Trace_routingClassifierTrace(TypedDict, closed=True):
    routingClassifierTrace: "aws_sdk_bedrock_agent_runtime.types.routing_classifier_trace.RoutingClassifierTrace"


class _Trace_failureTrace(TypedDict, closed=True):
    failureTrace: "aws_sdk_bedrock_agent_runtime.types.failure_trace.FailureTrace"


class _Trace_customOrchestrationTrace(TypedDict, closed=True):
    customOrchestrationTrace: "aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace.CustomOrchestrationTrace"


Trace: TypeAlias = (
    _Trace_guardrailTrace
    | _Trace_preProcessingTrace
    | _Trace_orchestrationTrace
    | _Trace_postProcessingTrace
    | _Trace_routingClassifierTrace
    | _Trace_failureTrace
    | _Trace_customOrchestrationTrace
)


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    if "guardrailTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_trace

        return {
            "guardrailTrace": aws_sdk_bedrock_agent_runtime.types.guardrail_trace.serialize_json(
                value["guardrailTrace"]
            )
        }
    elif "preProcessingTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.pre_processing_trace

        return {
            "preProcessingTrace": aws_sdk_bedrock_agent_runtime.types.pre_processing_trace.serialize_json(
                value["preProcessingTrace"]
            )
        }
    elif "orchestrationTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.orchestration_trace

        return {
            "orchestrationTrace": aws_sdk_bedrock_agent_runtime.types.orchestration_trace.serialize_json(
                value["orchestrationTrace"]
            )
        }
    elif "postProcessingTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.post_processing_trace

        return {
            "postProcessingTrace": aws_sdk_bedrock_agent_runtime.types.post_processing_trace.serialize_json(
                value["postProcessingTrace"]
            )
        }
    elif "routingClassifierTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.routing_classifier_trace

        return {
            "routingClassifierTrace": aws_sdk_bedrock_agent_runtime.types.routing_classifier_trace.serialize_json(
                value["routingClassifierTrace"]
            )
        }
    elif "failureTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.failure_trace

        return {
            "failureTrace": aws_sdk_bedrock_agent_runtime.types.failure_trace.serialize_json(
                value["failureTrace"]
            )
        }
    elif "customOrchestrationTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace

        return {
            "customOrchestrationTrace": aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace.serialize_json(
                value["customOrchestrationTrace"]
            )
        }
    else:
        raise SerializationError("Trace: no variant present")


def deserialize_json(data: dict) -> Trace:
    if "guardrailTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_trace

        return {
            "guardrailTrace": aws_sdk_bedrock_agent_runtime.types.guardrail_trace.deserialize_json(
                data["guardrailTrace"]
            )
        }
    elif "preProcessingTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.pre_processing_trace

        return {
            "preProcessingTrace": aws_sdk_bedrock_agent_runtime.types.pre_processing_trace.deserialize_json(
                data["preProcessingTrace"]
            )
        }
    elif "orchestrationTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.orchestration_trace

        return {
            "orchestrationTrace": aws_sdk_bedrock_agent_runtime.types.orchestration_trace.deserialize_json(
                data["orchestrationTrace"]
            )
        }
    elif "postProcessingTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.post_processing_trace

        return {
            "postProcessingTrace": aws_sdk_bedrock_agent_runtime.types.post_processing_trace.deserialize_json(
                data["postProcessingTrace"]
            )
        }
    elif "routingClassifierTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.routing_classifier_trace

        return {
            "routingClassifierTrace": aws_sdk_bedrock_agent_runtime.types.routing_classifier_trace.deserialize_json(
                data["routingClassifierTrace"]
            )
        }
    elif "failureTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.failure_trace

        return {
            "failureTrace": aws_sdk_bedrock_agent_runtime.types.failure_trace.deserialize_json(
                data["failureTrace"]
            )
        }
    elif "customOrchestrationTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace

        return {
            "customOrchestrationTrace": aws_sdk_bedrock_agent_runtime.types.custom_orchestration_trace.deserialize_json(
                data["customOrchestrationTrace"]
            )
        }
    else:
        raise DeserializationError("Trace: no recognized variant key")
