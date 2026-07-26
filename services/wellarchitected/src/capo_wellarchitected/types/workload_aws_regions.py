"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadAwsRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.aws_region

WorkloadAwsRegions: TypeAlias = list["capo_wellarchitected.types.aws_region.AwsRegion"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadAwsRegions) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadAwsRegions:
    return list(data)
