"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfEventVariableSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.event_variable_summary

ListOfEventVariableSummaries: TypeAlias = list[
    "capo_frauddetector.types.event_variable_summary.EventVariableSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEventVariableSummaries) -> list:
    import capo_frauddetector.types.event_variable_summary

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.event_variable_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEventVariableSummaries:
    import capo_frauddetector.types.event_variable_summary

    out: ListOfEventVariableSummaries = []
    for item in data:
        out.append(
            capo_frauddetector.types.event_variable_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
