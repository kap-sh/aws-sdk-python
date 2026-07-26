"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_summary

ModelSummaries: TypeAlias = list[
    "capo_lookoutequipment.types.model_summary.ModelSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelSummaries) -> list:
    import capo_lookoutequipment.types.model_summary

    out: list = []
    for item in value:
        out.append(
            capo_lookoutequipment.types.model_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ModelSummaries:
    import capo_lookoutequipment.types.model_summary

    out: ModelSummaries = []
    for item in data:
        out.append(
            capo_lookoutequipment.types.model_summary.deserialize_aws_json_1_0(item)
        )
    return out
