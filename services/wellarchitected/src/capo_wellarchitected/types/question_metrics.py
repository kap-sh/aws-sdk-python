"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.question_metric

QuestionMetrics: TypeAlias = list[
    "capo_wellarchitected.types.question_metric.QuestionMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionMetrics) -> list:
    import capo_wellarchitected.types.question_metric

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.question_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuestionMetrics:
    import capo_wellarchitected.types.question_metric

    out: QuestionMetrics = []
    for item in data:
        out.append(capo_wellarchitected.types.question_metric.deserialize_json(item))
    return out
