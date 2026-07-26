"""Generated from Smithy shape ``com.amazonaws.fsx#Snapshots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.snapshot

Snapshots: TypeAlias = list["capo_fsx.types.snapshot.Snapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshots) -> list:
    import capo_fsx.types.snapshot

    out: list = []
    for item in value:
        out.append(capo_fsx.types.snapshot.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Snapshots:
    import capo_fsx.types.snapshot

    out: Snapshots = []
    for item in data:
        out.append(capo_fsx.types.snapshot.deserialize_aws_json_1_1(item))
    return out
