"""Generated from Smithy shape ``com.amazonaws.connect#ListEvaluationFormsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_summary_list
    import aws_sdk_connect.types.next_token


class ListEvaluationFormsResponse(TypedDict):
    evaluation_form_summary_list: (
        "aws_sdk_connect.types.evaluation_form_summary_list.EvaluationFormSummaryList"
    )
    """<p>Provides details about a list of evaluation forms belonging to an instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationFormsResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_summary_list

    out["EvaluationFormSummaryList"] = (
        aws_sdk_connect.types.evaluation_form_summary_list.serialize_json(
            value["evaluation_form_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEvaluationFormsResponse:
    out: ListEvaluationFormsResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationFormSummaryList" in data:
        import aws_sdk_connect.types.evaluation_form_summary_list

        out["evaluation_form_summary_list"] = (
            aws_sdk_connect.types.evaluation_form_summary_list.deserialize_json(
                data["EvaluationFormSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListEvaluationFormsResponse.evaluation_form_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
