"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSNfsExportOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_nfs_export_option

OpenZFSNfsExportOptions: TypeAlias = list[
    "aws_sdk_fsx.types.open_zfs_nfs_export_option.OpenZFSNfsExportOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSNfsExportOptions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpenZFSNfsExportOptions:
    return list(data)
