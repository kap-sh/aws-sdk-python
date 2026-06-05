"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportImageTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_export_image_tasks_max_results
    import aws_sdk_ec2.types.export_image_task_id_list
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeExportImageTasksRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Filter tasks using the <code>task-state</code> filter and one of the following values: <code>active</code>, <code>completed</code>, <code>deleting</code>, or <code>deleted</code>.</p>"""
    export_image_task_ids: NotRequired[
        "aws_sdk_ec2.types.export_image_task_id_list.ExportImageTaskIdList"
    ]
    """<p>The IDs of the export image tasks.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_export_image_tasks_max_results.DescribeExportImageTasksMaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>A token that indicates the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeExportImageTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "export_image_task_ids" in value:
        import aws_sdk_ec2.types.export_image_task_id_list

        aws_sdk_ec2.types.export_image_task_id_list.serialize_ec2_query(
            value["export_image_task_ids"], pairs, f"{prefix}.ExportImageTaskIds"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeExportImageTasksRequest:
    out: DescribeExportImageTasksRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    if el.find("ExportImageTaskIds") is not None:
        import aws_sdk_ec2.types.export_image_task_id_list

        out["export_image_task_ids"] = (
            aws_sdk_ec2.types.export_image_task_id_list.deserialize_ec2_query(
                el, "ExportImageTaskIds"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
