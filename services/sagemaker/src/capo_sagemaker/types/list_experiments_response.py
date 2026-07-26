"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListExperimentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.experiment_summaries
    import capo_sagemaker.types.next_token


class ListExperimentsResponse(TypedDict, closed=True):
    experiment_summaries: NotRequired[
        "capo_sagemaker.types.experiment_summaries.ExperimentSummaries"
    ]
    """<p>A list of the summaries of your experiments.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of experiments, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExperimentsResponse) -> dict:
    out: dict = {}
    if "experiment_summaries" in value:
        import capo_sagemaker.types.experiment_summaries

        out["ExperimentSummaries"] = (
            capo_sagemaker.types.experiment_summaries.serialize_aws_json_1_1(
                value["experiment_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExperimentsResponse:
    out: ListExperimentsResponse = {}  # type: ignore[typeddict-item]
    if "ExperimentSummaries" in data:
        import capo_sagemaker.types.experiment_summaries

        out["experiment_summaries"] = (
            capo_sagemaker.types.experiment_summaries.deserialize_aws_json_1_1(
                data["ExperimentSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
