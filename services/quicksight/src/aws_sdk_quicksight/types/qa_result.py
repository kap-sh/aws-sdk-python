"""Generated from Smithy shape ``com.amazonaws.quicksight#QAResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_visual_result
    import aws_sdk_quicksight.types.generated_answer_result
    import aws_sdk_quicksight.types.qa_result_type


class QAResult(TypedDict):
    result_type: NotRequired["aws_sdk_quicksight.types.qa_result_type.QAResultType"]
    """<p>The type of QA result.</p>"""
    dashboard_visual: NotRequired[
        "aws_sdk_quicksight.types.dashboard_visual_result.DashboardVisualResult"
    ]
    """<p>The representation of a dashboard visual result.</p>"""
    generated_answer: NotRequired[
        "aws_sdk_quicksight.types.generated_answer_result.GeneratedAnswerResult"
    ]
    """<p>The representation of a generated answer result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QAResult) -> dict:
    out: dict = {}
    if "result_type" in value:
        import aws_sdk_quicksight.types.qa_result_type

        out["ResultType"] = aws_sdk_quicksight.types.qa_result_type.serialize_json(
            value["result_type"]
        )
    if "dashboard_visual" in value:
        import aws_sdk_quicksight.types.dashboard_visual_result

        out["DashboardVisual"] = (
            aws_sdk_quicksight.types.dashboard_visual_result.serialize_json(
                value["dashboard_visual"]
            )
        )
    if "generated_answer" in value:
        import aws_sdk_quicksight.types.generated_answer_result

        out["GeneratedAnswer"] = (
            aws_sdk_quicksight.types.generated_answer_result.serialize_json(
                value["generated_answer"]
            )
        )
    return out


def deserialize_json(data: dict) -> QAResult:
    out: QAResult = {}  # type: ignore[typeddict-item]
    if "ResultType" in data:
        import aws_sdk_quicksight.types.qa_result_type

        out["result_type"] = aws_sdk_quicksight.types.qa_result_type.deserialize_json(
            data["ResultType"]
        )
    if "DashboardVisual" in data:
        import aws_sdk_quicksight.types.dashboard_visual_result

        out["dashboard_visual"] = (
            aws_sdk_quicksight.types.dashboard_visual_result.deserialize_json(
                data["DashboardVisual"]
            )
        )
    if "GeneratedAnswer" in data:
        import aws_sdk_quicksight.types.generated_answer_result

        out["generated_answer"] = (
            aws_sdk_quicksight.types.generated_answer_result.deserialize_json(
                data["GeneratedAnswer"]
            )
        )
    return out
