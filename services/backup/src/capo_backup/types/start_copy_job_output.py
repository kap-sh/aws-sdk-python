"""Generated from Smithy shape ``com.amazonaws.backup#StartCopyJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.boolean2
    import capo_backup.types.string
    import capo_backup.types.timestamp


class StartCopyJobOutput(TypedDict, closed=True):
    copy_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a copy job.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a copy job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    is_parent: "capo_backup.types.boolean2.Boolean2"
    """<p>This is a returned boolean value indicating this is a parent (composite) copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCopyJobOutput) -> dict:
    out: dict = {}
    if "copy_job_id" in value:
        out["CopyJobId"] = value["copy_job_id"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    out["IsParent"] = value.get("is_parent", False)
    return out


def deserialize_json(data: dict) -> StartCopyJobOutput:
    out: StartCopyJobOutput = {}  # type: ignore[typeddict-item]
    if "CopyJobId" in data:
        out["copy_job_id"] = data["CopyJobId"]
    if "CreationDate" in data:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "IsParent" in data:
        out["is_parent"] = data["IsParent"]
    else:
        out["is_parent"] = False
    return out
