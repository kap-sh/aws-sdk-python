"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceEventSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_event_summary

InferenceEventSummaries: TypeAlias = list[
    "capo_lookoutequipment.types.inference_event_summary.InferenceEventSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceEventSummaries) -> list:
    import capo_lookoutequipment.types.inference_event_summary

    out: list = []
    for item in value:
        out.append(
            capo_lookoutequipment.types.inference_event_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InferenceEventSummaries:
    import capo_lookoutequipment.types.inference_event_summary

    out: InferenceEventSummaries = []
    for item in data:
        out.append(
            capo_lookoutequipment.types.inference_event_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
