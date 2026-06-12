"""Generated from Smithy shape ``com.amazonaws.iot#GetBehaviorModelTrainingSummariesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_model_training_summaries
    import aws_sdk_iot.types.next_token


class GetBehaviorModelTrainingSummariesResponse(TypedDict):
    summaries: NotRequired[
        "aws_sdk_iot.types.behavior_model_training_summaries.BehaviorModelTrainingSummaries"
    ]
    """<p> A list of all ML Detect behaviors and their model status for a given Security Profile. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBehaviorModelTrainingSummariesResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import aws_sdk_iot.types.behavior_model_training_summaries

        out["summaries"] = (
            aws_sdk_iot.types.behavior_model_training_summaries.serialize_json(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBehaviorModelTrainingSummariesResponse:
    out: GetBehaviorModelTrainingSummariesResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import aws_sdk_iot.types.behavior_model_training_summaries

        out["summaries"] = (
            aws_sdk_iot.types.behavior_model_training_summaries.deserialize_json(
                data["summaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
