"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelResolveToResourceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary

ComputationModelResolveToResourceSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary.ComputationModelResolveToResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelResolveToResourceSummaries) -> list:
    import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ComputationModelResolveToResourceSummaries:
    import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary

    out: ComputationModelResolveToResourceSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summary.deserialize_json(
                item
            )
        )
    return out
