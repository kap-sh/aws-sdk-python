"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadNonAwsRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload_non_aws_region

WorkloadNonAwsRegions: TypeAlias = list[
    "aws_sdk_wellarchitected.types.workload_non_aws_region.WorkloadNonAwsRegion"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadNonAwsRegions) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadNonAwsRegions:
    return list(data)
