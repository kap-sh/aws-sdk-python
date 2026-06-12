"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.best_practices
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.risk


class QuestionMetric(TypedDict):
    question_id: NotRequired["aws_sdk_wellarchitected.types.question_id.QuestionId"]
    risk: NotRequired["aws_sdk_wellarchitected.types.risk.Risk"]
    best_practices: NotRequired[
        "aws_sdk_wellarchitected.types.best_practices.BestPractices"
    ]
    """<p>The best practices, or choices, that have been identified as contributing to risk in a question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionMetric) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "risk" in value:
        import aws_sdk_wellarchitected.types.risk

        out["Risk"] = aws_sdk_wellarchitected.types.risk.serialize_json(value["risk"])
    if "best_practices" in value:
        import aws_sdk_wellarchitected.types.best_practices

        out["BestPractices"] = (
            aws_sdk_wellarchitected.types.best_practices.serialize_json(
                value["best_practices"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuestionMetric:
    out: QuestionMetric = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "Risk" in data:
        import aws_sdk_wellarchitected.types.risk

        out["risk"] = aws_sdk_wellarchitected.types.risk.deserialize_json(data["Risk"])
    if "BestPractices" in data:
        import aws_sdk_wellarchitected.types.best_practices

        out["best_practices"] = (
            aws_sdk_wellarchitected.types.best_practices.deserialize_json(
                data["BestPractices"]
            )
        )
    return out
