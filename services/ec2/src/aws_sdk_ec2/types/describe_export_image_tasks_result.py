"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportImageTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_image_task_list
    import aws_sdk_ec2.types.next_token


class DescribeExportImageTasksResult(TypedDict):
    export_image_tasks: NotRequired[
        "aws_sdk_ec2.types.export_image_task_list.ExportImageTaskList"
    ]
    """<p>Information about the export image tasks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeExportImageTasksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_image_tasks" in value:
        import aws_sdk_ec2.types.export_image_task_list

        aws_sdk_ec2.types.export_image_task_list.serialize_ec2_query(
            value["export_image_tasks"], pairs, f"{prefix}.ExportImageTaskSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeExportImageTasksResult:
    out: DescribeExportImageTasksResult = {}  # type: ignore[typeddict-item]
    if el.find("ExportImageTaskSet") is not None:
        import aws_sdk_ec2.types.export_image_task_list

        out["export_image_tasks"] = (
            aws_sdk_ec2.types.export_image_task_list.deserialize_ec2_query(
                el, "ExportImageTaskSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
