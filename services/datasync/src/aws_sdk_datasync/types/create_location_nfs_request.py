"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationNfsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.input_tag_list
    import aws_sdk_datasync.types.nfs_mount_options
    import aws_sdk_datasync.types.nfs_subdirectory
    import aws_sdk_datasync.types.on_prem_config
    import aws_sdk_datasync.types.server_hostname


class CreateLocationNfsRequest(TypedDict):
    subdirectory: "aws_sdk_datasync.types.nfs_subdirectory.NfsSubdirectory"
    r"""<p>Specifies the export path in your NFS file server that you want DataSync to mount.</p> <p>This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs\">Accessing NFS file servers</a>.</p>"""
    server_hostname: "aws_sdk_datasync.types.server_hostname.ServerHostname"
    """<p>Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.</p>"""
    on_prem_config: "aws_sdk_datasync.types.on_prem_config.OnPremConfig"
    r"""<p>Specifies the Amazon Resource Name (ARN) of the DataSync agent that can connect to your NFS file server.</p> <p>You can specify more than one agent. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents\">Using multiple DataSync agents</a>.</p>"""
    mount_options: NotRequired[
        "aws_sdk_datasync.types.nfs_mount_options.NfsMountOptions"
    ]
    """<p>Specifies the options that DataSync can use to mount your NFS file server.</p>"""
    tags: NotRequired["aws_sdk_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationNfsRequest) -> dict:
    out: dict = {}
    out["Subdirectory"] = value["subdirectory"]
    out["ServerHostname"] = value["server_hostname"]
    import aws_sdk_datasync.types.on_prem_config

    out["OnPremConfig"] = aws_sdk_datasync.types.on_prem_config.serialize_aws_json_1_1(
        value["on_prem_config"]
    )
    if "mount_options" in value:
        import aws_sdk_datasync.types.nfs_mount_options

        out["MountOptions"] = (
            aws_sdk_datasync.types.nfs_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    if "tags" in value:
        import aws_sdk_datasync.types.input_tag_list

        out["Tags"] = aws_sdk_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationNfsRequest:
    out: CreateLocationNfsRequest = {}  # type: ignore[typeddict-item]
    if "Subdirectory" in data:
        out["subdirectory"] = data["Subdirectory"]
    else:
        raise DeserializationError("CreateLocationNfsRequest.subdirectory required")
    if "ServerHostname" in data:
        out["server_hostname"] = data["ServerHostname"]
    else:
        raise DeserializationError("CreateLocationNfsRequest.server_hostname required")
    if "OnPremConfig" in data:
        import aws_sdk_datasync.types.on_prem_config

        out["on_prem_config"] = (
            aws_sdk_datasync.types.on_prem_config.deserialize_aws_json_1_1(
                data["OnPremConfig"]
            )
        )
    else:
        raise DeserializationError("CreateLocationNfsRequest.on_prem_config required")
    if "MountOptions" in data:
        import aws_sdk_datasync.types.nfs_mount_options

        out["mount_options"] = (
            aws_sdk_datasync.types.nfs_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_datasync.types.input_tag_list

        out["tags"] = aws_sdk_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
