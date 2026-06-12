"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.question_metric

QuestionMetrics: TypeAlias = list[
    "aws_sdk_wellarchitected.types.question_metric.QuestionMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionMetrics) -> list:
    import aws_sdk_wellarchitected.types.question_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.question_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuestionMetrics:
    import aws_sdk_wellarchitected.types.question_metric

    out: QuestionMetrics = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.question_metric.deserialize_json(item))
    return out
