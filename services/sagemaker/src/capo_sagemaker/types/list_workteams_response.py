"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListWorkteamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.workteams


class ListWorkteamsResponse(TypedDict, closed=True):
    workteams: NotRequired["capo_sagemaker.types.workteams.Workteams"]
    """<p>An array of <code>Workteam</code> objects, each describing a work team.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of work teams, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkteamsResponse) -> dict:
    out: dict = {}
    if "workteams" in value:
        import capo_sagemaker.types.workteams

        out["Workteams"] = capo_sagemaker.types.workteams.serialize_aws_json_1_1(
            value["workteams"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkteamsResponse:
    out: ListWorkteamsResponse = {}  # type: ignore[typeddict-item]
    if "Workteams" in data:
        import capo_sagemaker.types.workteams

        out["workteams"] = capo_sagemaker.types.workteams.deserialize_aws_json_1_1(
            data["Workteams"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
