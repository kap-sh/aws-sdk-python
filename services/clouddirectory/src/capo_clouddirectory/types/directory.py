"""Generated from Smithy shape ``com.amazonaws.clouddirectory#Directory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.date
    import capo_clouddirectory.types.directory_arn
    import capo_clouddirectory.types.directory_name
    import capo_clouddirectory.types.directory_state


class Directory(TypedDict, closed=True):
    name: NotRequired["capo_clouddirectory.types.directory_name.DirectoryName"]
    """<p>The name of the directory.</p>"""
    directory_arn: NotRequired["capo_clouddirectory.types.directory_arn.DirectoryArn"]
    """<p>The Amazon Resource Name (ARN) that is associated with the directory. For more information, see <a>arns</a>.</p>"""
    state: NotRequired["capo_clouddirectory.types.directory_state.DirectoryState"]
    """<p>The state of the directory. Can be either <code>Enabled</code>, <code>Disabled</code>, or <code>Deleted</code>.</p>"""
    creation_date_time: NotRequired["capo_clouddirectory.types.date.Date"]
    """<p>The date and time when the directory was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Directory) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "directory_arn" in value:
        out["DirectoryArn"] = value["directory_arn"]
    if "state" in value:
        import capo_clouddirectory.types.directory_state

        out["State"] = capo_clouddirectory.types.directory_state.serialize_json(
            value["state"]
        )
    if "creation_date_time" in value:
        import capo_clouddirectory.types.date

        out["CreationDateTime"] = capo_clouddirectory.types.date.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> Directory:
    out: Directory = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    if "State" in data:
        import capo_clouddirectory.types.directory_state

        out["state"] = capo_clouddirectory.types.directory_state.deserialize_json(
            data["State"]
        )
    if "CreationDateTime" in data:
        import capo_clouddirectory.types.date

        out["creation_date_time"] = capo_clouddirectory.types.date.deserialize_json(
            data["CreationDateTime"]
        )
    return out
