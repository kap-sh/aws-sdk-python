"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_task_id_string_list
    import capo_ec2.types.filter_list


class DescribeExportTasksRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>the filters for the export tasks.</p>"""
    export_task_ids: NotRequired[
        "capo_ec2.types.export_task_id_string_list.ExportTaskIdStringList"
    ]
    """<p>The export task IDs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeExportTasksRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "export_task_ids" in value:
        import capo_ec2.types.export_task_id_string_list

        capo_ec2.types.export_task_id_string_list.serialize_ec2_query(
            value["export_task_ids"], pairs, f"{key_prefix}ExportTaskId"
        )


def deserialize_ec2_query(el: Element) -> DescribeExportTasksRequest:
    out: DescribeExportTasksRequest = {}  # type: ignore[typeddict-item]
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    if el.find("ExportTaskId") is not None:
        import capo_ec2.types.export_task_id_string_list

        out["export_task_ids"] = (
            capo_ec2.types.export_task_id_string_list.deserialize_ec2_query(
                el, "ExportTaskId"
            )
        )
    return out
