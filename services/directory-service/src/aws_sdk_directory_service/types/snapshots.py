"""Generated from Smithy shape ``com.amazonaws.directoryservice#Snapshots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.snapshot

Snapshots: TypeAlias = list["aws_sdk_directory_service.types.snapshot.Snapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshots) -> list:
    import aws_sdk_directory_service.types.snapshot

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.snapshot.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Snapshots:
    import aws_sdk_directory_service.types.snapshot

    out: Snapshots = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.snapshot.deserialize_aws_json_1_1(item)
        )
    return out
