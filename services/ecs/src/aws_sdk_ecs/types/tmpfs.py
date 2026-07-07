"""Generated from Smithy shape ``com.amazonaws.ecs#Tmpfs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class Tmpfs(TypedDict, closed=True):
    container_path: "aws_sdk_ecs.types.string.String"
    """<p>The absolute file path where the tmpfs volume is to be mounted.</p>"""
    size: "aws_sdk_ecs.types.integer.Integer"
    """<p>The maximum size (in MiB) of the tmpfs volume.</p>"""
    mount_options: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    r"""<p>The list of tmpfs volume mount options.</p> <p>Valid values: <code>\"defaults\" | \"ro\" | \"rw\" | \"suid\" | \"nosuid\" | \"dev\" | \"nodev\" | \"exec\" | \"noexec\" | \"sync\" | \"async\" | \"dirsync\" | \"remount\" | \"mand\" | \"nomand\" | \"atime\" | \"noatime\" | \"diratime\" | \"nodiratime\" | \"bind\" | \"rbind\" | \"unbindable\" | \"runbindable\" | \"private\" | \"rprivate\" | \"shared\" | \"rshared\" | \"slave\" | \"rslave\" | \"relatime\" | \"norelatime\" | \"strictatime\" | \"nostrictatime\" | \"mode\" | \"uid\" | \"gid\" | \"nr_inodes\" | \"nr_blocks\" | \"mpol\"</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tmpfs) -> dict:
    out: dict = {}
    out["containerPath"] = value["container_path"]
    out["size"] = value.get("size", 0)
    if "mount_options" in value:
        import aws_sdk_ecs.types.string_list

        out["mountOptions"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["mount_options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Tmpfs:
    out: Tmpfs = {}  # type: ignore[typeddict-item]
    if "containerPath" in data:
        out["container_path"] = data["containerPath"]
    else:
        raise DeserializationError("Tmpfs.container_path required")
    if "size" in data:
        out["size"] = data["size"]
    else:
        out["size"] = 0
    if "mountOptions" in data:
        import aws_sdk_ecs.types.string_list

        out["mount_options"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["mountOptions"]
        )
    return out
