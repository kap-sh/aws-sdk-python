"""Generated from Smithy shape ``com.amazonaws.efs#RootDirectory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.creation_info
    import capo_efs.types.path


class RootDirectory(TypedDict, closed=True):
    path: NotRequired["capo_efs.types.path.Path"]
    """<p>Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the <code>CreationInfo</code>.</p>"""
    creation_info: NotRequired["capo_efs.types.creation_info.CreationInfo"]
    """<p>(Optional) Specifies the POSIX IDs and permissions to apply to the access point's <code>RootDirectory</code>. If the <code>RootDirectory</code> > <code>Path</code> specified does not exist, EFS creates the root directory using the <code>CreationInfo</code> settings when a client connects to an access point. When specifying the <code>CreationInfo</code>, you must provide values for all properties. </p> <important> <p>If you do not provide <code>CreationInfo</code> and the specified <code>RootDirectory</code> > <code>Path</code> does not exist, attempts to mount the file system using the access point will fail.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: RootDirectory) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "creation_info" in value:
        import capo_efs.types.creation_info

        out["CreationInfo"] = capo_efs.types.creation_info.serialize_json(
            value["creation_info"]
        )
    return out


def deserialize_json(data: dict) -> RootDirectory:
    out: RootDirectory = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    if "CreationInfo" in data:
        import capo_efs.types.creation_info

        out["creation_info"] = capo_efs.types.creation_info.deserialize_json(
            data["CreationInfo"]
        )
    return out
