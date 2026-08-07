"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeResourceScanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.percentage_completed
    import capo_cloudformation.types.resource_scan_id
    import capo_cloudformation.types.resource_scan_status
    import capo_cloudformation.types.resource_scan_status_reason
    import capo_cloudformation.types.resource_types
    import capo_cloudformation.types.resources_read
    import capo_cloudformation.types.resources_scanned
    import capo_cloudformation.types.scan_filters
    import capo_cloudformation.types.timestamp


class DescribeResourceScanOutput(TypedDict, closed=True):
    resource_scan_id: NotRequired[
        "capo_cloudformation.types.resource_scan_id.ResourceScanId"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource scan. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:resourceScan/${Id}</code>. An example is <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:resourceScan/<i>f5b490f7-7ed4-428a-aa06-31ff25db0772</i> </code>.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.resource_scan_status.ResourceScanStatus"
    ]
    """<p>Status of the resource scan.</p> <dl> <dt> IN_PROGRESS </dt> <dd> <p>The resource scan is still in progress.</p> </dd> <dt> COMPLETE </dt> <dd> <p>The resource scan is complete.</p> </dd> <dt> EXPIRED </dt> <dd> <p>The resource scan has expired.</p> </dd> <dt> FAILED </dt> <dd> <p>The resource scan has failed.</p> </dd> </dl>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.resource_scan_status_reason.ResourceScanStatusReason"
    ]
    """<p>The reason for the resource scan status, providing more information if a failure happened.</p>"""
    start_time: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The time that the resource scan was started.</p>"""
    end_time: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The time that the resource scan was finished.</p>"""
    percentage_completed: NotRequired[
        "capo_cloudformation.types.percentage_completed.PercentageCompleted"
    ]
    """<p>The percentage of the resource scan that has been completed.</p>"""
    resource_types: NotRequired[
        "capo_cloudformation.types.resource_types.ResourceTypes"
    ]
    """<p>The list of resource types for the specified scan. Resource types are only available for scans with a <code>Status</code> set to <code>COMPLETE</code> or <code>FAILED </code>.</p>"""
    resources_scanned: NotRequired[
        "capo_cloudformation.types.resources_scanned.ResourcesScanned"
    ]
    """<p>The number of resources that were listed. This is only available for scans with a <code>Status</code> set to <code>COMPLETE</code>, <code>EXPIRED</code>, or <code>FAILED </code>.</p>"""
    resources_read: NotRequired[
        "capo_cloudformation.types.resources_read.ResourcesRead"
    ]
    """<p>The number of resources that were read. This is only available for scans with a <code>Status</code> set to <code>COMPLETE</code>, <code>EXPIRED</code>, or <code>FAILED</code>.</p> <note> <p>This field may be 0 if the resource scan failed with a <code>ResourceScanLimitExceededException</code>.</p> </note>"""
    scan_filters: NotRequired["capo_cloudformation.types.scan_filters.ScanFilters"]
    """<p>The scan filters that were used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeResourceScanOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_scan_id" in value:
        pairs.append((f"{key_prefix}ResourceScanId", str(value["resource_scan_id"])))
    if "status" in value:
        import capo_cloudformation.types.resource_scan_status

        capo_cloudformation.types.resource_scan_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "start_time" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "percentage_completed" in value:
        pairs.append(
            (f"{key_prefix}PercentageCompleted", str(value["percentage_completed"]))
        )
    if "resource_types" in value:
        import capo_cloudformation.types.resource_types

        capo_cloudformation.types.resource_types.serialize_query(
            value["resource_types"], pairs, f"{key_prefix}ResourceTypes"
        )
    if "resources_scanned" in value:
        pairs.append((f"{key_prefix}ResourcesScanned", str(value["resources_scanned"])))
    if "resources_read" in value:
        pairs.append((f"{key_prefix}ResourcesRead", str(value["resources_read"])))
    if "scan_filters" in value:
        import capo_cloudformation.types.scan_filters

        capo_cloudformation.types.scan_filters.serialize_query(
            value["scan_filters"], pairs, f"{key_prefix}ScanFilters"
        )


def deserialize_query(el: Element) -> DescribeResourceScanOutput:
    out: DescribeResourceScanOutput = {}  # type: ignore[typeddict-item]
    child_resource_scan_id = el.find("ResourceScanId")
    if child_resource_scan_id is not None:
        out["resource_scan_id"] = str(child_resource_scan_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.resource_scan_status

        out["status"] = (
            capo_cloudformation.types.resource_scan_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_cloudformation.types.timestamp

        out["start_time"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_cloudformation.types.timestamp

        out["end_time"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_end_time
        )
    child_percentage_completed = el.find("PercentageCompleted")
    if child_percentage_completed is not None:
        out["percentage_completed"] = float(child_percentage_completed.text or "")
    child_resource_types = el.find("ResourceTypes")
    if child_resource_types is not None:
        import capo_cloudformation.types.resource_types

        out["resource_types"] = (
            capo_cloudformation.types.resource_types.deserialize_query(
                child_resource_types
            )
        )
    child_resources_scanned = el.find("ResourcesScanned")
    if child_resources_scanned is not None:
        out["resources_scanned"] = int(child_resources_scanned.text or "")
    child_resources_read = el.find("ResourcesRead")
    if child_resources_read is not None:
        out["resources_read"] = int(child_resources_read.text or "")
    child_scan_filters = el.find("ScanFilters")
    if child_scan_filters is not None:
        import capo_cloudformation.types.scan_filters

        out["scan_filters"] = capo_cloudformation.types.scan_filters.deserialize_query(
            child_scan_filters
        )
    return out
