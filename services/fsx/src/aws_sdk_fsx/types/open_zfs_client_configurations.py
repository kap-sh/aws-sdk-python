"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSClientConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_client_configuration

OpenZFSClientConfigurations: TypeAlias = list[
    "aws_sdk_fsx.types.open_zfs_client_configuration.OpenZFSClientConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSClientConfigurations) -> list:
    import aws_sdk_fsx.types.open_zfs_client_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.open_zfs_client_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OpenZFSClientConfigurations:
    import aws_sdk_fsx.types.open_zfs_client_configuration

    out: OpenZFSClientConfigurations = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.open_zfs_client_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
