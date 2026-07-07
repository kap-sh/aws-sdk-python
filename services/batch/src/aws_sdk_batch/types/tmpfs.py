"""Generated from Smithy shape ``com.amazonaws.batch#Tmpfs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list


class Tmpfs(TypedDict, closed=True):
    container_path: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The absolute file path in the container where the <code>tmpfs</code> volume is mounted.</p>"""
    size: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The size (in MiB) of the <code>tmpfs</code> volume.</p>"""
    mount_options: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    r"""<p>The list of <code>tmpfs</code> volume mount options.</p> <p>Valid values: \"<code>defaults</code>\" | \"<code>ro</code>\" | \"<code>rw</code>\" | \"<code>suid</code>\" | \"<code>nosuid</code>\" | \"<code>dev</code>\" | \"<code>nodev</code>\" | \"<code>exec</code>\" | \"<code>noexec</code>\" | \"<code>sync</code>\" | \"<code>async</code>\" | \"<code>dirsync</code>\" | \"<code>remount</code>\" | \"<code>mand</code>\" | \"<code>nomand</code>\" | \"<code>atime</code>\" | \"<code>noatime</code>\" | \"<code>diratime</code>\" | \"<code>nodiratime</code>\" | \"<code>bind</code>\" | \"<code>rbind\" | \"unbindable\" | \"runbindable\" | \"private\" | \"rprivate\" | \"shared\" | \"rshared\" | \"slave\" | \"rslave\" | \"relatime</code>\" | \"<code>norelatime</code>\" | \"<code>strictatime</code>\" | \"<code>nostrictatime</code>\" | \"<code>mode</code>\" | \"<code>uid</code>\" | \"<code>gid</code>\" | \"<code>nr_inodes</code>\" | \"<code>nr_blocks</code>\" | \"<code>mpol</code>\"</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tmpfs) -> dict:
    out: dict = {}
    if "container_path" in value:
        out["containerPath"] = value["container_path"]
    if "size" in value:
        out["size"] = value["size"]
    if "mount_options" in value:
        import aws_sdk_batch.types.string_list

        out["mountOptions"] = aws_sdk_batch.types.string_list.serialize_json(
            value["mount_options"]
        )
    return out


def deserialize_json(data: dict) -> Tmpfs:
    out: Tmpfs = {}  # type: ignore[typeddict-item]
    if "containerPath" in data:
        out["container_path"] = data["containerPath"]
    if "size" in data:
        out["size"] = data["size"]
    if "mountOptions" in data:
        import aws_sdk_batch.types.string_list

        out["mount_options"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["mountOptions"]
        )
    return out
