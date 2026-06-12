"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceScanSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.percentage_completed
    import aws_sdk_cloudformation.types.resource_scan_id
    import aws_sdk_cloudformation.types.resource_scan_status
    import aws_sdk_cloudformation.types.resource_scan_status_reason
    import aws_sdk_cloudformation.types.scan_type
    import aws_sdk_cloudformation.types.timestamp


class ResourceScanSummary(TypedDict):
    resource_scan_id: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_id.ResourceScanId"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource scan.</p>"""
    status: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_status.ResourceScanStatus"
    ]
    """<p>Status of the resource scan.</p> <dl> <dt> IN_PROGRESS </dt> <dd> <p>The resource scan is still in progress.</p> </dd> <dt> COMPLETE </dt> <dd> <p>The resource scan is complete.</p> </dd> <dt> EXPIRED </dt> <dd> <p>The resource scan has expired.</p> </dd> <dt> FAILED </dt> <dd> <p>The resource scan has failed.</p> </dd> </dl>"""
    status_reason: NotRequired[
        "aws_sdk_cloudformation.types.resource_scan_status_reason.ResourceScanStatusReason"
    ]
    """<p>The reason for the resource scan status, providing more information if a failure happened.</p>"""
    start_time: NotRequired["aws_sdk_cloudformation.types.timestamp.Timestamp"]
    """<p>The time that the resource scan was started.</p>"""
    end_time: NotRequired["aws_sdk_cloudformation.types.timestamp.Timestamp"]
    """<p>The time that the resource scan was finished.</p>"""
    percentage_completed: NotRequired[
        "aws_sdk_cloudformation.types.percentage_completed.PercentageCompleted"
    ]
    """<p>The percentage of the resource scan that has been completed.</p>"""
    scan_type: NotRequired["aws_sdk_cloudformation.types.scan_type.ScanType"]
    """<p>The scan type that has been completed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceScanSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_scan_id" in value:
        pairs.append((f"{prefix}.ResourceScanId", str(value["resource_scan_id"])))
    if "status" in value:
        import aws_sdk_cloudformation.types.resource_scan_status

        aws_sdk_cloudformation.types.resource_scan_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_reason" in value:
        pairs.append((f"{prefix}.StatusReason", str(value["status_reason"])))
    if "start_time" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "percentage_completed" in value:
        pairs.append(
            (f"{prefix}.PercentageCompleted", str(value["percentage_completed"]))
        )
    if "scan_type" in value:
        import aws_sdk_cloudformation.types.scan_type

        aws_sdk_cloudformation.types.scan_type.serialize_query(
            value["scan_type"], pairs, f"{prefix}.ScanType"
        )


def deserialize_query(el: Element) -> ResourceScanSummary:
    out: ResourceScanSummary = {}  # type: ignore[typeddict-item]
    child_resource_scan_id = el.find("ResourceScanId")
    if child_resource_scan_id is not None:
        out["resource_scan_id"] = str(child_resource_scan_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudformation.types.resource_scan_status

        out["status"] = (
            aws_sdk_cloudformation.types.resource_scan_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["start_time"] = aws_sdk_cloudformation.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["end_time"] = aws_sdk_cloudformation.types.timestamp.deserialize_query(
            child_end_time
        )
    child_percentage_completed = el.find("PercentageCompleted")
    if child_percentage_completed is not None:
        out["percentage_completed"] = float(child_percentage_completed.text or "")
    child_scan_type = el.find("ScanType")
    if child_scan_type is not None:
        import aws_sdk_cloudformation.types.scan_type

        out["scan_type"] = aws_sdk_cloudformation.types.scan_type.deserialize_query(
            child_scan_type
        )
    return out
