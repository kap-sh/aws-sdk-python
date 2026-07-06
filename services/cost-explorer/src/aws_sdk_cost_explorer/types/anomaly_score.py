"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_double


class AnomalyScore(TypedDict, closed=True):
    max_score: "aws_sdk_cost_explorer.types.generic_double.GenericDouble"
    """<p>The maximum score that's observed during the <code>AnomalyDateInterval</code>. </p>"""
    current_score: "aws_sdk_cost_explorer.types.generic_double.GenericDouble"
    """<p>The last observed score. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyScore) -> dict:
    out: dict = {}
    out["MaxScore"] = value.get("max_score", 0)
    out["CurrentScore"] = value.get("current_score", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalyScore:
    out: AnomalyScore = {}  # type: ignore[typeddict-item]
    if "MaxScore" in data:
        out["max_score"] = data["MaxScore"]
    else:
        out["max_score"] = 0
    if "CurrentScore" in data:
        out["current_score"] = data["CurrentScore"]
    else:
        out["current_score"] = 0
    return out
