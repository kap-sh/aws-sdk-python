"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadApplications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.application_arn

WorkloadApplications: TypeAlias = list[
    "capo_wellarchitected.types.application_arn.ApplicationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadApplications) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadApplications:
    return list(data)
