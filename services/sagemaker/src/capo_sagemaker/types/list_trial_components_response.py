"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrialComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.trial_component_summaries


class ListTrialComponentsResponse(TypedDict, closed=True):
    trial_component_summaries: NotRequired[
        "capo_sagemaker.types.trial_component_summaries.TrialComponentSummaries"
    ]
    """<p>A list of the summaries of your trial components.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of components, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrialComponentsResponse) -> dict:
    out: dict = {}
    if "trial_component_summaries" in value:
        import capo_sagemaker.types.trial_component_summaries

        out["TrialComponentSummaries"] = (
            capo_sagemaker.types.trial_component_summaries.serialize_aws_json_1_1(
                value["trial_component_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrialComponentsResponse:
    out: ListTrialComponentsResponse = {}  # type: ignore[typeddict-item]
    if "TrialComponentSummaries" in data:
        import capo_sagemaker.types.trial_component_summaries

        out["trial_component_summaries"] = (
            capo_sagemaker.types.trial_component_summaries.deserialize_aws_json_1_1(
                data["TrialComponentSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
