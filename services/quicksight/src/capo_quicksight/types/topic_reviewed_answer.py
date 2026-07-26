"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicReviewedAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.answer_id
    import capo_quicksight.types.arn
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.topic_ir
    import capo_quicksight.types.topic_template
    import capo_quicksight.types.topic_visual


class TopicReviewedAnswer(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the reviewed answer.</p>"""
    answer_id: "capo_quicksight.types.answer_id.AnswerId"
    """<p>The answer ID of the reviewed answer.</p>"""
    dataset_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Dataset ARN for the <code>TopicReviewedAnswer</code>.</p>"""
    question: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The question for the <code>TopicReviewedAnswer</code>.</p>"""
    mir: NotRequired["capo_quicksight.types.topic_ir.TopicIR"]
    """<p>The mir for the <code>TopicReviewedAnswer</code>.</p>"""
    primary_visual: NotRequired["capo_quicksight.types.topic_visual.TopicVisual"]
    """<p>The primary visual for the <code>TopicReviewedAnswer</code>.</p>"""
    template: NotRequired["capo_quicksight.types.topic_template.TopicTemplate"]
    """<p>The template for the <code>TopicReviewedAnswer</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicReviewedAnswer) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["AnswerId"] = value["answer_id"]
    out["DatasetArn"] = value["dataset_arn"]
    out["Question"] = value["question"]
    if "mir" in value:
        import capo_quicksight.types.topic_ir

        out["Mir"] = capo_quicksight.types.topic_ir.serialize_json(value["mir"])
    if "primary_visual" in value:
        import capo_quicksight.types.topic_visual

        out["PrimaryVisual"] = capo_quicksight.types.topic_visual.serialize_json(
            value["primary_visual"]
        )
    if "template" in value:
        import capo_quicksight.types.topic_template

        out["Template"] = capo_quicksight.types.topic_template.serialize_json(
            value["template"]
        )
    return out


def deserialize_json(data: dict) -> TopicReviewedAnswer:
    out: TopicReviewedAnswer = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AnswerId" in data:
        out["answer_id"] = data["AnswerId"]
    else:
        raise DeserializationError("TopicReviewedAnswer.answer_id required")
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("TopicReviewedAnswer.dataset_arn required")
    if "Question" in data:
        out["question"] = data["Question"]
    else:
        raise DeserializationError("TopicReviewedAnswer.question required")
    if "Mir" in data:
        import capo_quicksight.types.topic_ir

        out["mir"] = capo_quicksight.types.topic_ir.deserialize_json(data["Mir"])
    if "PrimaryVisual" in data:
        import capo_quicksight.types.topic_visual

        out["primary_visual"] = capo_quicksight.types.topic_visual.deserialize_json(
            data["PrimaryVisual"]
        )
    if "Template" in data:
        import capo_quicksight.types.topic_template

        out["template"] = capo_quicksight.types.topic_template.deserialize_json(
            data["Template"]
        )
    return out
