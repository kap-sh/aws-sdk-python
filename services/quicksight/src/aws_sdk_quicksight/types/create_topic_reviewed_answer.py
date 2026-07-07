"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTopicReviewedAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.answer_id
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.topic_ir
    import aws_sdk_quicksight.types.topic_template
    import aws_sdk_quicksight.types.topic_visual


class CreateTopicReviewedAnswer(TypedDict, closed=True):
    answer_id: "aws_sdk_quicksight.types.answer_id.AnswerId"
    """<p>The answer ID for the <code>CreateTopicReviewedAnswer</code>.</p>"""
    dataset_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Dataset arn for the <code>CreateTopicReviewedAnswer</code>.</p>"""
    question: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The Question to be created.</p>"""
    mir: NotRequired["aws_sdk_quicksight.types.topic_ir.TopicIR"]
    """<p>The Mir for the <code>CreateTopicReviewedAnswer</code>.</p>"""
    primary_visual: NotRequired["aws_sdk_quicksight.types.topic_visual.TopicVisual"]
    """<p>The <code>PrimaryVisual</code> for the <code>CreateTopicReviewedAnswer</code>.</p>"""
    template: NotRequired["aws_sdk_quicksight.types.topic_template.TopicTemplate"]
    """<p>The template for the <code>CreateTopicReviewedAnswer</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicReviewedAnswer) -> dict:
    out: dict = {}
    out["AnswerId"] = value["answer_id"]
    out["DatasetArn"] = value["dataset_arn"]
    out["Question"] = value["question"]
    if "mir" in value:
        import aws_sdk_quicksight.types.topic_ir

        out["Mir"] = aws_sdk_quicksight.types.topic_ir.serialize_json(value["mir"])
    if "primary_visual" in value:
        import aws_sdk_quicksight.types.topic_visual

        out["PrimaryVisual"] = aws_sdk_quicksight.types.topic_visual.serialize_json(
            value["primary_visual"]
        )
    if "template" in value:
        import aws_sdk_quicksight.types.topic_template

        out["Template"] = aws_sdk_quicksight.types.topic_template.serialize_json(
            value["template"]
        )
    return out


def deserialize_json(data: dict) -> CreateTopicReviewedAnswer:
    out: CreateTopicReviewedAnswer = {}  # type: ignore[typeddict-item]
    if "AnswerId" in data:
        out["answer_id"] = data["AnswerId"]
    else:
        raise DeserializationError("CreateTopicReviewedAnswer.answer_id required")
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("CreateTopicReviewedAnswer.dataset_arn required")
    if "Question" in data:
        out["question"] = data["Question"]
    else:
        raise DeserializationError("CreateTopicReviewedAnswer.question required")
    if "Mir" in data:
        import aws_sdk_quicksight.types.topic_ir

        out["mir"] = aws_sdk_quicksight.types.topic_ir.deserialize_json(data["Mir"])
    if "PrimaryVisual" in data:
        import aws_sdk_quicksight.types.topic_visual

        out["primary_visual"] = aws_sdk_quicksight.types.topic_visual.deserialize_json(
            data["PrimaryVisual"]
        )
    if "Template" in data:
        import aws_sdk_quicksight.types.topic_template

        out["template"] = aws_sdk_quicksight.types.topic_template.deserialize_json(
            data["Template"]
        )
    return out
