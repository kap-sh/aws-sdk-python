"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestResults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.evaluator_metric_list


class ABTestResults(TypedDict):
    analysis_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the analysis was performed.</p>"""
    evaluator_metrics: (
        "aws_sdk_bedrock_agentcore.types.evaluator_metric_list.EvaluatorMetricList"
    )
    """<p>The per-evaluator metrics comparing control and treatment variants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ABTestResults) -> dict:
    out: dict = {}
    if "analysis_timestamp" in value:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["analysisTimestamp"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["analysis_timestamp"]
            )
        )
    import aws_sdk_bedrock_agentcore.types.evaluator_metric_list

    out["evaluatorMetrics"] = (
        aws_sdk_bedrock_agentcore.types.evaluator_metric_list.serialize_json(
            value["evaluator_metrics"]
        )
    )
    return out


def deserialize_json(data: dict) -> ABTestResults:
    out: ABTestResults = {}  # type: ignore[typeddict-item]
    if "analysisTimestamp" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["analysis_timestamp"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["analysisTimestamp"]
            )
        )
    if "evaluatorMetrics" in data:
        import aws_sdk_bedrock_agentcore.types.evaluator_metric_list

        out["evaluator_metrics"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_metric_list.deserialize_json(
                data["evaluatorMetrics"]
            )
        )
    else:
        raise DeserializationError("ABTestResults.evaluator_metrics required")
    return out
