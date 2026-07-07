"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ApplyGuardrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_action
    import aws_sdk_bedrock_runtime.types.guardrail_assessment_list
    import aws_sdk_bedrock_runtime.types.guardrail_coverage
    import aws_sdk_bedrock_runtime.types.guardrail_output_content_list
    import aws_sdk_bedrock_runtime.types.guardrail_usage


class ApplyGuardrailResponse(TypedDict, closed=True):
    usage: "aws_sdk_bedrock_runtime.types.guardrail_usage.GuardrailUsage"
    """<p>The usage details in the response from the guardrail.</p>"""
    action: "aws_sdk_bedrock_runtime.types.guardrail_action.GuardrailAction"
    """<p>The action taken in the response from the guardrail.</p>"""
    action_reason: NotRequired["str"]
    """<p>The reason for the action taken when harmful content is detected.</p>"""
    outputs: "aws_sdk_bedrock_runtime.types.guardrail_output_content_list.GuardrailOutputContentList"
    """<p>The output details in the response from the guardrail.</p>"""
    assessments: "aws_sdk_bedrock_runtime.types.guardrail_assessment_list.GuardrailAssessmentList"
    """<p>The assessment details in the response from the guardrail.</p>"""
    guardrail_coverage: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_coverage.GuardrailCoverage"
    ]
    """<p>The guardrail coverage details in the apply guardrail response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyGuardrailResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.guardrail_usage

    out["usage"] = aws_sdk_bedrock_runtime.types.guardrail_usage.serialize_json(
        value["usage"]
    )
    import aws_sdk_bedrock_runtime.types.guardrail_action

    out["action"] = aws_sdk_bedrock_runtime.types.guardrail_action.serialize_json(
        value["action"]
    )
    if "action_reason" in value:
        out["actionReason"] = value["action_reason"]
    import aws_sdk_bedrock_runtime.types.guardrail_output_content_list

    out["outputs"] = (
        aws_sdk_bedrock_runtime.types.guardrail_output_content_list.serialize_json(
            value["outputs"]
        )
    )
    import aws_sdk_bedrock_runtime.types.guardrail_assessment_list

    out["assessments"] = (
        aws_sdk_bedrock_runtime.types.guardrail_assessment_list.serialize_json(
            value["assessments"]
        )
    )
    if "guardrail_coverage" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_coverage

        out["guardrailCoverage"] = (
            aws_sdk_bedrock_runtime.types.guardrail_coverage.serialize_json(
                value["guardrail_coverage"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplyGuardrailResponse:
    out: ApplyGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "usage" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_usage

        out["usage"] = aws_sdk_bedrock_runtime.types.guardrail_usage.deserialize_json(
            data["usage"]
        )
    else:
        raise DeserializationError("ApplyGuardrailResponse.usage required")
    if "action" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_action

        out["action"] = aws_sdk_bedrock_runtime.types.guardrail_action.deserialize_json(
            data["action"]
        )
    else:
        raise DeserializationError("ApplyGuardrailResponse.action required")
    if "actionReason" in data:
        out["action_reason"] = data["actionReason"]
    if "outputs" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_output_content_list

        out["outputs"] = (
            aws_sdk_bedrock_runtime.types.guardrail_output_content_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        raise DeserializationError("ApplyGuardrailResponse.outputs required")
    if "assessments" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_assessment_list

        out["assessments"] = (
            aws_sdk_bedrock_runtime.types.guardrail_assessment_list.deserialize_json(
                data["assessments"]
            )
        )
    else:
        raise DeserializationError("ApplyGuardrailResponse.assessments required")
    if "guardrailCoverage" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_coverage

        out["guardrail_coverage"] = (
            aws_sdk_bedrock_runtime.types.guardrail_coverage.deserialize_json(
                data["guardrailCoverage"]
            )
        )
    return out
