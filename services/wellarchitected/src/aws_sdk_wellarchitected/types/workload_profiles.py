"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.workload_profile

WorkloadProfiles: TypeAlias = list[
    "aws_sdk_wellarchitected.types.workload_profile.WorkloadProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadProfiles) -> list:
    import aws_sdk_wellarchitected.types.workload_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.workload_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkloadProfiles:
    import aws_sdk_wellarchitected.types.workload_profile

    out: WorkloadProfiles = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.workload_profile.deserialize_json(item)
        )
    return out
