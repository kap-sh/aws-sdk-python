"""Generated from Smithy shape ``com.amazonaws.quicksight#GeneratedAnswerResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.answer_id
    import aws_sdk_quicksight.types.generated_answer_status
    import aws_sdk_quicksight.types.qa_query_text
    import aws_sdk_quicksight.types.qa_url
    import aws_sdk_quicksight.types.question_id
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.topic_id


class GeneratedAnswerResult(TypedDict):
    question_text: NotRequired["aws_sdk_quicksight.types.qa_query_text.QAQueryText"]
    """<p>The question text.</p>"""
    answer_status: NotRequired[
        "aws_sdk_quicksight.types.generated_answer_status.GeneratedAnswerStatus"
    ]
    """<p>The answer status of the generated answer.</p>"""
    topic_id: NotRequired["aws_sdk_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic.</p>"""
    topic_name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the topic.</p>"""
    restatement: NotRequired["aws_sdk_quicksight.types.qa_query_text.QAQueryText"]
    """<p>The restatement for the answer.</p>"""
    question_id: NotRequired["aws_sdk_quicksight.types.question_id.QuestionId"]
    """<p>The ID of the question.</p>"""
    answer_id: NotRequired["aws_sdk_quicksight.types.answer_id.AnswerId"]
    """<p>The ID of the answer.</p>"""
    question_url: NotRequired["aws_sdk_quicksight.types.qa_url.QAUrl"]
    """<p>The URL of the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedAnswerResult) -> dict:
    out: dict = {}
    if "question_text" in value:
        out["QuestionText"] = value["question_text"]
    if "answer_status" in value:
        import aws_sdk_quicksight.types.generated_answer_status

        out["AnswerStatus"] = (
            aws_sdk_quicksight.types.generated_answer_status.serialize_json(
                value["answer_status"]
            )
        )
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "restatement" in value:
        out["Restatement"] = value["restatement"]
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "answer_id" in value:
        out["AnswerId"] = value["answer_id"]
    if "question_url" in value:
        out["QuestionUrl"] = value["question_url"]
    return out


def deserialize_json(data: dict) -> GeneratedAnswerResult:
    out: GeneratedAnswerResult = {}  # type: ignore[typeddict-item]
    if "QuestionText" in data:
        out["question_text"] = data["QuestionText"]
    if "AnswerStatus" in data:
        import aws_sdk_quicksight.types.generated_answer_status

        out["answer_status"] = (
            aws_sdk_quicksight.types.generated_answer_status.deserialize_json(
                data["AnswerStatus"]
            )
        )
    if "TopicId" in data:
        out["topic_id"] = data["TopicId"]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    if "Restatement" in data:
        out["restatement"] = data["Restatement"]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "AnswerId" in data:
        out["answer_id"] = data["AnswerId"]
    if "QuestionUrl" in data:
        out["question_url"] = data["QuestionUrl"]
    return out
