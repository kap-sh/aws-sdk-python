"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListSubscribedWorkteamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.subscribed_workteams


class ListSubscribedWorkteamsResponse(TypedDict, closed=True):
    subscribed_workteams: NotRequired[
        "capo_sagemaker.types.subscribed_workteams.SubscribedWorkteams"
    ]
    """<p>An array of <code>Workteam</code> objects, each describing a work team.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of work teams, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSubscribedWorkteamsResponse) -> dict:
    out: dict = {}
    if "subscribed_workteams" in value:
        import capo_sagemaker.types.subscribed_workteams

        out["SubscribedWorkteams"] = (
            capo_sagemaker.types.subscribed_workteams.serialize_aws_json_1_1(
                value["subscribed_workteams"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSubscribedWorkteamsResponse:
    out: ListSubscribedWorkteamsResponse = {}  # type: ignore[typeddict-item]
    if "SubscribedWorkteams" in data:
        import capo_sagemaker.types.subscribed_workteams

        out["subscribed_workteams"] = (
            capo_sagemaker.types.subscribed_workteams.deserialize_aws_json_1_1(
                data["SubscribedWorkteams"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
