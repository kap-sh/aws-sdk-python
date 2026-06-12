"""Generated from Smithy shape ``com.amazonaws.connect#ListEvaluationFormVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_version_summary_list
    import aws_sdk_connect.types.next_token


class ListEvaluationFormVersionsResponse(TypedDict):
    evaluation_form_version_summary_list: "aws_sdk_connect.types.evaluation_form_version_summary_list.EvaluationFormVersionSummaryList"
    """<p>Provides details about a list of evaluation forms belonging to an instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationFormVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_version_summary_list

    out["EvaluationFormVersionSummaryList"] = (
        aws_sdk_connect.types.evaluation_form_version_summary_list.serialize_json(
            value["evaluation_form_version_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEvaluationFormVersionsResponse:
    out: ListEvaluationFormVersionsResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationFormVersionSummaryList" in data:
        import aws_sdk_connect.types.evaluation_form_version_summary_list

        out["evaluation_form_version_summary_list"] = (
            aws_sdk_connect.types.evaluation_form_version_summary_list.deserialize_json(
                data["EvaluationFormVersionSummaryList"]
            )
        )
    else:
        raise DeserializationError(
            "ListEvaluationFormVersionsResponse.evaluation_form_version_summary_list required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
