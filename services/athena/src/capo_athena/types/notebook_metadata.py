"""Generated from Smithy shape ``com.amazonaws.athena#NotebookMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.date
    import capo_athena.types.notebook_id
    import capo_athena.types.notebook_name
    import capo_athena.types.notebook_type
    import capo_athena.types.work_group_name


class NotebookMetadata(TypedDict, closed=True):
    notebook_id: NotRequired["capo_athena.types.notebook_id.NotebookId"]
    """<p>The notebook ID.</p>"""
    name: NotRequired["capo_athena.types.notebook_name.NotebookName"]
    """<p>The name of the notebook.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the Spark enabled workgroup to which the notebook belongs.</p>"""
    creation_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The time when the notebook was created.</p>"""
    type: NotRequired["capo_athena.types.notebook_type.NotebookType"]
    """<p>The type of notebook. Currently, the only valid type is <code>IPYNB</code>.</p>"""
    last_modified_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The time when the notebook was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookMetadata) -> dict:
    out: dict = {}
    if "notebook_id" in value:
        out["NotebookId"] = value["notebook_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    if "creation_time" in value:
        import capo_athena.types.date

        out["CreationTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "type" in value:
        import capo_athena.types.notebook_type

        out["Type"] = capo_athena.types.notebook_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "last_modified_time" in value:
        import capo_athena.types.date

        out["LastModifiedTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookMetadata:
    out: NotebookMetadata = {}  # type: ignore[typeddict-item]
    if "NotebookId" in data:
        out["notebook_id"] = data["NotebookId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    if "CreationTime" in data:
        import capo_athena.types.date

        out["creation_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "Type" in data:
        import capo_athena.types.notebook_type

        out["type"] = capo_athena.types.notebook_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "LastModifiedTime" in data:
        import capo_athena.types.date

        out["last_modified_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    return out
