"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrialsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.trial_summaries


class ListTrialsResponse(TypedDict, closed=True):
    trial_summaries: NotRequired["capo_sagemaker.types.trial_summaries.TrialSummaries"]
    """<p>A list of the summaries of your trials.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of trials, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrialsResponse) -> dict:
    out: dict = {}
    if "trial_summaries" in value:
        import capo_sagemaker.types.trial_summaries

        out["TrialSummaries"] = (
            capo_sagemaker.types.trial_summaries.serialize_aws_json_1_1(
                value["trial_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrialsResponse:
    out: ListTrialsResponse = {}  # type: ignore[typeddict-item]
    if "TrialSummaries" in data:
        import capo_sagemaker.types.trial_summaries

        out["trial_summaries"] = (
            capo_sagemaker.types.trial_summaries.deserialize_aws_json_1_1(
                data["TrialSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
