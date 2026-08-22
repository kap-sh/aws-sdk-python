"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorStatistics``."""

from typing_extensions import NotRequired, TypedDict


class EvaluatorStatistics(TypedDict, closed=True):
    average_score: NotRequired["float"]
    """<p>The average score across all evaluated sessions for this evaluator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorStatistics) -> dict:
    out: dict = {}
    if "average_score" in value:
        out["averageScore"] = (
            "NaN"
            if value["average_score"] != value["average_score"]
            else "Infinity"
            if value["average_score"] == float("inf")
            else "-Infinity"
            if value["average_score"] == float("-inf")
            else value["average_score"]
        )
    return out


def deserialize_json(data: dict) -> EvaluatorStatistics:
    out: EvaluatorStatistics = {}  # type: ignore[typeddict-item]
    if data.get("averageScore") is not None:
        out["average_score"] = float(data["averageScore"])
    return out
