"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSNfsExport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_client_configurations


class OpenZFSNfsExport(TypedDict):
    client_configurations: NotRequired[
        "aws_sdk_fsx.types.open_zfs_client_configurations.OpenZFSClientConfigurations"
    ]
    """<p>A list of configuration objects that contain the client and options for mounting the OpenZFS file system. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSNfsExport) -> dict:
    out: dict = {}
    if "client_configurations" in value:
        import aws_sdk_fsx.types.open_zfs_client_configurations

        out["ClientConfigurations"] = (
            aws_sdk_fsx.types.open_zfs_client_configurations.serialize_aws_json_1_1(
                value["client_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSNfsExport:
    out: OpenZFSNfsExport = {}  # type: ignore[typeddict-item]
    if "ClientConfigurations" in data:
        import aws_sdk_fsx.types.open_zfs_client_configurations

        out["client_configurations"] = (
            aws_sdk_fsx.types.open_zfs_client_configurations.deserialize_aws_json_1_1(
                data["ClientConfigurations"]
            )
        )
    return out
