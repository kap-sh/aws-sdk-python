"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelDataBindingUsageSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_data_binding_usage_summary

ComputationModelDataBindingUsageSummaries: TypeAlias = list[
    "capo_iotsitewise.types.computation_model_data_binding_usage_summary.ComputationModelDataBindingUsageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelDataBindingUsageSummaries) -> list:
    import capo_iotsitewise.types.computation_model_data_binding_usage_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.computation_model_data_binding_usage_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ComputationModelDataBindingUsageSummaries:
    import capo_iotsitewise.types.computation_model_data_binding_usage_summary

    out: ComputationModelDataBindingUsageSummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.computation_model_data_binding_usage_summary.deserialize_json(
                item
            )
        )
    return out
