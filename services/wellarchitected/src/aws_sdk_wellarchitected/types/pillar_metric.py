"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.question_metrics
    import aws_sdk_wellarchitected.types.risk_counts


class PillarMetric(TypedDict, closed=True):
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    risk_counts: NotRequired["aws_sdk_wellarchitected.types.risk_counts.RiskCounts"]
    questions: NotRequired[
        "aws_sdk_wellarchitected.types.question_metrics.QuestionMetrics"
    ]
    """<p>The questions that have been identified as risks in the pillar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PillarMetric) -> dict:
    out: dict = {}
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "risk_counts" in value:
        import aws_sdk_wellarchitected.types.risk_counts

        out["RiskCounts"] = aws_sdk_wellarchitected.types.risk_counts.serialize_json(
            value["risk_counts"]
        )
    if "questions" in value:
        import aws_sdk_wellarchitected.types.question_metrics

        out["Questions"] = (
            aws_sdk_wellarchitected.types.question_metrics.serialize_json(
                value["questions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PillarMetric:
    out: PillarMetric = {}  # type: ignore[typeddict-item]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "RiskCounts" in data:
        import aws_sdk_wellarchitected.types.risk_counts

        out["risk_counts"] = aws_sdk_wellarchitected.types.risk_counts.deserialize_json(
            data["RiskCounts"]
        )
    if "Questions" in data:
        import aws_sdk_wellarchitected.types.question_metrics

        out["questions"] = (
            aws_sdk_wellarchitected.types.question_metrics.deserialize_json(
                data["Questions"]
            )
        )
    return out
