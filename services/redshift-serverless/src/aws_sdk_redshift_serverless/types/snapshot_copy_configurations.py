"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#SnapshotCopyConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.snapshot_copy_configuration

SnapshotCopyConfigurations: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.snapshot_copy_configuration.SnapshotCopyConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotCopyConfigurations) -> list:
    import aws_sdk_redshift_serverless.types.snapshot_copy_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.snapshot_copy_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotCopyConfigurations:
    import aws_sdk_redshift_serverless.types.snapshot_copy_configuration

    out: SnapshotCopyConfigurations = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.snapshot_copy_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
