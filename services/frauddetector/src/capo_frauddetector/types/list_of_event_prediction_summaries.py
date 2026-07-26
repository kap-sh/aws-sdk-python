"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfEventPredictionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.event_prediction_summary

ListOfEventPredictionSummaries: TypeAlias = list[
    "capo_frauddetector.types.event_prediction_summary.EventPredictionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEventPredictionSummaries) -> list:
    import capo_frauddetector.types.event_prediction_summary

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.event_prediction_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEventPredictionSummaries:
    import capo_frauddetector.types.event_prediction_summary

    out: ListOfEventPredictionSummaries = []
    for item in data:
        out.append(
            capo_frauddetector.types.event_prediction_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
