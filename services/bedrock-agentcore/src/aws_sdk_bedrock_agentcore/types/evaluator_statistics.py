"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorStatistics``."""

from typing import TypedDict
from typing_extensions import NotRequired

class EvaluatorStatistics(TypedDict):
    average_score: NotRequired["float"]
    """<p>The average score across all evaluated sessions for this evaluator.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorStatistics) -> dict:
    out: dict = {}
    if "average_score" in value:
        out["averageScore"] = value["average_score"]
    return out


def deserialize_json(data: dict) -> EvaluatorStatistics:
    out: EvaluatorStatistics = {}  # type: ignore[typeddict-item]
    if "averageScore" in data:
        out["average_score"] = data["averageScore"]
    return out