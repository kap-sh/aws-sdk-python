"""Generated from Smithy shape ``com.amazonaws.ec2#ImportSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_task_detail
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ImportSnapshotResult(TypedDict, closed=True):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the import snapshot task.</p>"""
    import_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the import snapshot task.</p>"""
    snapshot_task_detail: NotRequired[
        "aws_sdk_ec2.types.snapshot_task_detail.SnapshotTaskDetail"
    ]
    """<p>Information about the import snapshot task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the import snapshot task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "import_task_id" in value:
        pairs.append((f"{prefix}.ImportTaskId", str(value["import_task_id"])))
    if "snapshot_task_detail" in value:
        import aws_sdk_ec2.types.snapshot_task_detail

        aws_sdk_ec2.types.snapshot_task_detail.serialize_ec2_query(
            value["snapshot_task_detail"], pairs, f"{prefix}.SnapshotTaskDetail"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> ImportSnapshotResult:
    out: ImportSnapshotResult = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_import_task_id = el.find("ImportTaskId")
    if child_import_task_id is not None:
        out["import_task_id"] = str(child_import_task_id.text or "")
    child_snapshot_task_detail = el.find("SnapshotTaskDetail")
    if child_snapshot_task_detail is not None:
        import aws_sdk_ec2.types.snapshot_task_detail

        out["snapshot_task_detail"] = (
            aws_sdk_ec2.types.snapshot_task_detail.deserialize_ec2_query(
                child_snapshot_task_detail
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
