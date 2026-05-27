"""Generated from Smithy shape ``com.amazonaws.ecs#Tmpfs``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class Tmpfs(TypedDict):
    container_path: "aws_sdk_ecs.types.string.String"
    """<p>The absolute file path where the tmpfs volume is to be mounted.</p>"""
    size: "aws_sdk_ecs.types.integer.Integer"
    """<p>The maximum size (in MiB) of the tmpfs volume.</p>"""
    mount_options: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of tmpfs volume mount options.</p> <p>Valid values: <code>\"defaults\" | \"ro\" | \"rw\" | \"suid\" | \"nosuid\" | \"dev\" | \"nodev\" | \"exec\" | \"noexec\" | \"sync\" | \"async\" | \"dirsync\" | \"remount\" | \"mand\" | \"nomand\" | \"atime\" | \"noatime\" | \"diratime\" | \"nodiratime\" | \"bind\" | \"rbind\" | \"unbindable\" | \"runbindable\" | \"private\" | \"rprivate\" | \"shared\" | \"rshared\" | \"slave\" | \"rslave\" | \"relatime\" | \"norelatime\" | \"strictatime\" | \"nostrictatime\" | \"mode\" | \"uid\" | \"gid\" | \"nr_inodes\" | \"nr_blocks\" | \"mpol\"</code> </p>"""
