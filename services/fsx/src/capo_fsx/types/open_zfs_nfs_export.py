"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSNfsExport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.open_zfs_client_configurations


class OpenZFSNfsExport(TypedDict, closed=True):
    client_configurations: NotRequired[
        "capo_fsx.types.open_zfs_client_configurations.OpenZFSClientConfigurations"
    ]
    """<p>A list of configuration objects that contain the client and options for mounting the OpenZFS file system. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSNfsExport) -> dict:
    out: dict = {}
    if "client_configurations" in value:
        import capo_fsx.types.open_zfs_client_configurations

        out["ClientConfigurations"] = (
            capo_fsx.types.open_zfs_client_configurations.serialize_aws_json_1_1(
                value["client_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSNfsExport:
    out: OpenZFSNfsExport = {}  # type: ignore[typeddict-item]
    if "ClientConfigurations" in data:
        import capo_fsx.types.open_zfs_client_configurations

        out["client_configurations"] = (
            capo_fsx.types.open_zfs_client_configurations.deserialize_aws_json_1_1(
                data["ClientConfigurations"]
            )
        )
    return out
