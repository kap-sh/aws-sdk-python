"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportSnapshotTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_snapshot_task_list
    import aws_sdk_ec2.types.string


class DescribeImportSnapshotTasksResult(TypedDict):
    import_snapshot_tasks: NotRequired[
        "aws_sdk_ec2.types.import_snapshot_task_list.ImportSnapshotTaskList"
    ]
    """<p>A list of zero or more import snapshot tasks that are currently active or were completed or canceled in the previous 7 days.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeImportSnapshotTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "import_snapshot_tasks" in value:
        import aws_sdk_ec2.types.import_snapshot_task_list

        aws_sdk_ec2.types.import_snapshot_task_list.serialize_ec2_query(
            value["import_snapshot_tasks"], pairs, f"{prefix}.ImportSnapshotTaskSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeImportSnapshotTasksResult:
    out: DescribeImportSnapshotTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("ImportSnapshotTaskSet") is not None:
        import aws_sdk_ec2.types.import_snapshot_task_list

        out["import_snapshot_tasks"] = (
            aws_sdk_ec2.types.import_snapshot_task_list.deserialize_ec2_query(
                el, "ImportSnapshotTaskSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
