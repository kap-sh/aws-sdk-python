"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelResolveToResourceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_resolve_to_resource_summary

ComputationModelResolveToResourceSummaries: TypeAlias = list[
    "capo_iotsitewise.types.computation_model_resolve_to_resource_summary.ComputationModelResolveToResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelResolveToResourceSummaries) -> list:
    import capo_iotsitewise.types.computation_model_resolve_to_resource_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.computation_model_resolve_to_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ComputationModelResolveToResourceSummaries:
    import capo_iotsitewise.types.computation_model_resolve_to_resource_summary

    out: ComputationModelResolveToResourceSummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.computation_model_resolve_to_resource_summary.deserialize_json(
                item
            )
        )
    return out
