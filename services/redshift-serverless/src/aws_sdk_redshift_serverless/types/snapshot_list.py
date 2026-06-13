"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#SnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.snapshot

SnapshotList: TypeAlias = list["aws_sdk_redshift_serverless.types.snapshot.Snapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotList) -> list:
    import aws_sdk_redshift_serverless.types.snapshot

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.snapshot.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotList:
    import aws_sdk_redshift_serverless.types.snapshot

    out: SnapshotList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.snapshot.deserialize_aws_json_1_1(item)
        )
    return out
