"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationResultContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.context
    import aws_sdk_bedrock_agentcore.types.evaluation_error_code
    import aws_sdk_bedrock_agentcore.types.evaluation_error_message
    import aws_sdk_bedrock_agentcore.types.evaluation_explanation
    import aws_sdk_bedrock_agentcore.types.evaluator_arn
    import aws_sdk_bedrock_agentcore.types.evaluator_id
    import aws_sdk_bedrock_agentcore.types.evaluator_name
    import aws_sdk_bedrock_agentcore.types.ignored_reference_input_fields
    import aws_sdk_bedrock_agentcore.types.token_usage


class EvaluationResultContent(TypedDict):
    evaluator_arn: "aws_sdk_bedrock_agentcore.types.evaluator_arn.EvaluatorArn"
    """<p> The Amazon Resource Name (ARN) of the evaluator used to generate this result. For custom evaluators, this is the full ARN; for built-in evaluators, this follows the pattern <code>Builtin.{EvaluatorName}</code>. </p>"""
    evaluator_id: "aws_sdk_bedrock_agentcore.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator that produced this result. This matches the <code>evaluatorId</code> provided in the evaluation request and can be used to identify which evaluator generated specific results. </p>"""
    evaluator_name: "aws_sdk_bedrock_agentcore.types.evaluator_name.EvaluatorName"
    r"""<p> The human-readable name of the evaluator used for this evaluation. For built-in evaluators, this is the descriptive name (e.g., \"Helpfulness\", \"Correctness\"); for custom evaluators, this is the user-defined name. </p>"""
    explanation: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_explanation.EvaluationExplanation"
    ]
    """<p> The detailed explanation provided by the evaluator describing the reasoning behind the assigned score. This qualitative feedback helps understand why specific ratings were given and provides actionable insights for improvement. </p>"""
    context: "aws_sdk_bedrock_agentcore.types.context.Context"
    """<p> The contextual information associated with this evaluation result, including span context details that identify the specific traces and sessions that were evaluated. </p>"""
    value: NotRequired["float"]
    """<p> The numerical score assigned by the evaluator according to its configured rating scale. For numerical scales, this is a decimal value within the defined range. This field is not allowed for categorical scales. </p>"""
    label: NotRequired["str"]
    r"""<p> The categorical label assigned by the evaluator when using a categorical rating scale. This provides a human-readable description of the evaluation result (e.g., \"Excellent\", \"Good\", \"Poor\") corresponding to the numerical value. For numerical scales, this field is optional and provides a natural language explanation of what the value means (e.g., value 0.5 = \"Somewhat Helpful\"). </p>"""
    token_usage: NotRequired["aws_sdk_bedrock_agentcore.types.token_usage.TokenUsage"]
    """<p> The token consumption statistics for this evaluation, including input tokens, output tokens, and total tokens used by the underlying language model during the evaluation process. </p>"""
    error_message: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_error_message.EvaluationErrorMessage"
    ]
    """<p> The error message describing what went wrong if the evaluation failed. Provides detailed information about evaluation failures to help diagnose and resolve issues with evaluator configuration or input data. </p>"""
    error_code: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_error_code.EvaluationErrorCode"
    ]
    """<p> The error code indicating the type of failure that occurred during evaluation. Used to programmatically identify and handle different categories of evaluation errors. </p>"""
    ignored_reference_input_fields: NotRequired[
        "aws_sdk_bedrock_agentcore.types.ignored_reference_input_fields.IgnoredReferenceInputFields"
    ]
    """<p> The list of reference input field names that were provided but not used by the evaluator. Helps identify which ground truth data was not consumed during evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationResultContent) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    out["evaluatorId"] = value["evaluator_id"]
    out["evaluatorName"] = value["evaluator_name"]
    if "explanation" in value:
        out["explanation"] = value["explanation"]
    import aws_sdk_bedrock_agentcore.types.context

    out["context"] = aws_sdk_bedrock_agentcore.types.context.serialize_json(
        value["context"]
    )
    if "value" in value:
        out["value"] = value["value"]
    if "label" in value:
        out["label"] = value["label"]
    if "token_usage" in value:
        import aws_sdk_bedrock_agentcore.types.token_usage

        out["tokenUsage"] = aws_sdk_bedrock_agentcore.types.token_usage.serialize_json(
            value["token_usage"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "ignored_reference_input_fields" in value:
        import aws_sdk_bedrock_agentcore.types.ignored_reference_input_fields

        out["ignoredReferenceInputFields"] = (
            aws_sdk_bedrock_agentcore.types.ignored_reference_input_fields.serialize_json(
                value["ignored_reference_input_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationResultContent:
    out: EvaluationResultContent = {}  # type: ignore[typeddict-item]
    if "evaluatorArn" in data:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        raise DeserializationError("EvaluationResultContent.evaluator_arn required")
    if "evaluatorId" in data:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        raise DeserializationError("EvaluationResultContent.evaluator_id required")
    if "evaluatorName" in data:
        out["evaluator_name"] = data["evaluatorName"]
    else:
        raise DeserializationError("EvaluationResultContent.evaluator_name required")
    if "explanation" in data:
        out["explanation"] = data["explanation"]
    if "context" in data:
        import aws_sdk_bedrock_agentcore.types.context

        out["context"] = aws_sdk_bedrock_agentcore.types.context.deserialize_json(
            data["context"]
        )
    else:
        raise DeserializationError("EvaluationResultContent.context required")
    if "value" in data:
        out["value"] = data["value"]
    if "label" in data:
        out["label"] = data["label"]
    if "tokenUsage" in data:
        import aws_sdk_bedrock_agentcore.types.token_usage

        out["token_usage"] = (
            aws_sdk_bedrock_agentcore.types.token_usage.deserialize_json(
                data["tokenUsage"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "ignoredReferenceInputFields" in data:
        import aws_sdk_bedrock_agentcore.types.ignored_reference_input_fields

        out["ignored_reference_input_fields"] = (
            aws_sdk_bedrock_agentcore.types.ignored_reference_input_fields.deserialize_json(
                data["ignoredReferenceInputFields"]
            )
        )
    return out
