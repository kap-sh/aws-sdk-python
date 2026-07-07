"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSClientConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.open_zfs_clients
    import aws_sdk_fsx.types.open_zfs_nfs_export_options


class OpenZFSClientConfiguration(TypedDict, closed=True):
    clients: NotRequired["aws_sdk_fsx.types.open_zfs_clients.OpenZFSClients"]
    """<p>A value that specifies who can mount the file system. You can provide a wildcard character (<code>*</code>), an IP address (<code>0.0.0.0</code>), or a CIDR address (<code>192.0.2.0/24</code>). By default, Amazon FSx uses the wildcard character when specifying the client. </p>"""
    options: NotRequired[
        "aws_sdk_fsx.types.open_zfs_nfs_export_options.OpenZFSNfsExportOptions"
    ]
    r"""<p>The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the <a href=\"https://linux.die.net/man/5/exports\">exports(5) - Linux man page</a>. When choosing your options, consider the following:</p> <ul> <li> <p> <code>crossmnt</code> is used by default. If you don't specify <code>crossmnt</code> when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory.</p> </li> <li> <p> <code>sync</code> is used by default. If you instead specify <code>async</code>, the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSClientConfiguration) -> dict:
    out: dict = {}
    if "clients" in value:
        out["Clients"] = value["clients"]
    if "options" in value:
        import aws_sdk_fsx.types.open_zfs_nfs_export_options

        out["Options"] = (
            aws_sdk_fsx.types.open_zfs_nfs_export_options.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSClientConfiguration:
    out: OpenZFSClientConfiguration = {}  # type: ignore[typeddict-item]
    if "Clients" in data:
        out["clients"] = data["Clients"]
    if "Options" in data:
        import aws_sdk_fsx.types.open_zfs_nfs_export_options

        out["options"] = (
            aws_sdk_fsx.types.open_zfs_nfs_export_options.deserialize_aws_json_1_1(
                data["Options"]
            )
        )
    return out
