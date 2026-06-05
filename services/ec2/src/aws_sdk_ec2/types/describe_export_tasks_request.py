"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_id_string_list
    import aws_sdk_ec2.types.filter_list


class DescribeExportTasksRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>the filters for the export tasks.</p>"""
    export_task_ids: NotRequired[
        "aws_sdk_ec2.types.export_task_id_string_list.ExportTaskIdStringList"
    ]
    """<p>The export task IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeExportTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "export_task_ids" in value:
        import aws_sdk_ec2.types.export_task_id_string_list

        aws_sdk_ec2.types.export_task_id_string_list.serialize_ec2_query(
            value["export_task_ids"], pairs, f"{prefix}.ExportTaskId"
        )


def deserialize_ec2_query(el: Element) -> DescribeExportTasksRequest:
    out: DescribeExportTasksRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    if el.find("ExportTaskId") is not None:
        import aws_sdk_ec2.types.export_task_id_string_list

        out["export_task_ids"] = (
            aws_sdk_ec2.types.export_task_id_string_list.deserialize_ec2_query(
                el, "ExportTaskId"
            )
        )
    return out
