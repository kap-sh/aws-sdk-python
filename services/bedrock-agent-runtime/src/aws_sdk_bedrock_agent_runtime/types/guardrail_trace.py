"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTrace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_action
    import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list
    import aws_sdk_bedrock_agent_runtime.types.metadata
    import aws_sdk_bedrock_agent_runtime.types.trace_id


class GuardrailTrace(TypedDict, closed=True):
    action: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_action.GuardrailAction"
    ]
    """<p>The trace action details used with the Guardrail.</p>"""
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The details of the trace Id used in the Guardrail Trace.</p>"""
    input_assessments: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list.GuardrailAssessmentList"
    ]
    """<p>The details of the input assessments used in the Guardrail Trace.</p>"""
    output_assessments: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list.GuardrailAssessmentList"
    ]
    """<p>The details of the output assessments used in the Guardrail Trace.</p>"""
    metadata: NotRequired["aws_sdk_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the Guardrail output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTrace) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_action.serialize_json(
                value["action"]
            )
        )
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "input_assessments" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list

        out["inputAssessments"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list.serialize_json(
                value["input_assessments"]
            )
        )
    if "output_assessments" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list

        out["outputAssessments"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list.serialize_json(
                value["output_assessments"]
            )
        )
    if "metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailTrace:
    out: GuardrailTrace = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_action

        out["action"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_action.deserialize_json(
                data["action"]
            )
        )
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    if "inputAssessments" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list

        out["input_assessments"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list.deserialize_json(
                data["inputAssessments"]
            )
        )
    if "outputAssessments" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list

        out["output_assessments"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_assessment_list.deserialize_json(
                data["outputAssessments"]
            )
        )
    if "metadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata

        out["metadata"] = aws_sdk_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out
