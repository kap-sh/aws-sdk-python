"""Generated from Smithy shape ``com.amazonaws.kendra#FaqStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.indexed_question_answers_count


class FaqStatistics(TypedDict, closed=True):
    indexed_question_answers_count: (
        "capo_kendra.types.indexed_question_answers_count.IndexedQuestionAnswersCount"
    )
    """<p>The total number of FAQ questions and answers for an index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqStatistics) -> dict:
    out: dict = {}
    out["IndexedQuestionAnswersCount"] = value.get("indexed_question_answers_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> FaqStatistics:
    out: FaqStatistics = {}  # type: ignore[typeddict-item]
    if "IndexedQuestionAnswersCount" in data:
        out["indexed_question_answers_count"] = data["IndexedQuestionAnswersCount"]
    else:
        out["indexed_question_answers_count"] = 0
    return out
