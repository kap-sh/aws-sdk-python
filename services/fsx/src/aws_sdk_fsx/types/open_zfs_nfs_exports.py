"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSNfsExports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_nfs_export

OpenZFSNfsExports: TypeAlias = list[
    "aws_sdk_fsx.types.open_zfs_nfs_export.OpenZFSNfsExport"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSNfsExports) -> list:
    import aws_sdk_fsx.types.open_zfs_nfs_export

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.open_zfs_nfs_export.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpenZFSNfsExports:
    import aws_sdk_fsx.types.open_zfs_nfs_export

    out: OpenZFSNfsExports = []
    for item in data:
        out.append(aws_sdk_fsx.types.open_zfs_nfs_export.deserialize_aws_json_1_1(item))
    return out
