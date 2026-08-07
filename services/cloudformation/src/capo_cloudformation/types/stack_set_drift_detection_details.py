"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetDriftDetectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.drifted_stack_instances_count
    import capo_cloudformation.types.failed_stack_instances_count
    import capo_cloudformation.types.in_progress_stack_instances_count
    import capo_cloudformation.types.in_sync_stack_instances_count
    import capo_cloudformation.types.stack_set_drift_detection_status
    import capo_cloudformation.types.stack_set_drift_status
    import capo_cloudformation.types.timestamp
    import capo_cloudformation.types.total_stack_instances_count


class StackSetDriftDetectionDetails(TypedDict, closed=True):
    drift_status: NotRequired[
        "capo_cloudformation.types.stack_set_drift_status.StackSetDriftStatus"
    ]
    """<p>Status of the StackSet's actual configuration compared to its expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the StackSet differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the StackSet for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All of the stack instances belonging to the StackSet stack match the expected template and parameter configuration.</p> </li> </ul>"""
    drift_detection_status: NotRequired[
        "capo_cloudformation.types.stack_set_drift_detection_status.StackSetDriftDetectionStatus"
    ]
    """<p>The status of the StackSet drift detection operation.</p> <ul> <li> <p> <code>COMPLETED</code>: The drift detection operation completed without failing on any stack instances.</p> </li> <li> <p> <code>FAILED</code>: The drift detection operation exceeded the specified failure tolerance.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: The drift detection operation completed without exceeding the failure tolerance for the operation.</p> </li> <li> <p> <code>IN_PROGRESS</code>: The drift detection operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the drift detection operation.</p> </li> </ul>"""
    last_drift_check_timestamp: NotRequired[
        "capo_cloudformation.types.timestamp.Timestamp"
    ]
    """<p>Most recent time when CloudFormation performed a drift detection operation on the StackSet. This value will be <code>NULL</code> for any StackSet that drift detection hasn't yet been performed on.</p>"""
    total_stack_instances_count: NotRequired[
        "capo_cloudformation.types.total_stack_instances_count.TotalStackInstancesCount"
    ]
    """<p>The total number of stack instances belonging to this StackSet.</p> <p>The total number of stack instances is equal to the total of:</p> <ul> <li> <p>Stack instances that match the StackSet configuration.</p> </li> <li> <p>Stack instances that have drifted from the StackSet configuration.</p> </li> <li> <p>Stack instances where the drift detection operation has failed.</p> </li> <li> <p>Stack instances currently being checked for drift.</p> </li> </ul>"""
    drifted_stack_instances_count: NotRequired[
        "capo_cloudformation.types.drifted_stack_instances_count.DriftedStackInstancesCount"
    ]
    """<p>The number of stack instances that have drifted from the expected template and parameter configuration of the StackSet. A stack instance is considered to have drifted if one or more of the resources in the associated stack don't match their expected configuration.</p>"""
    in_sync_stack_instances_count: NotRequired[
        "capo_cloudformation.types.in_sync_stack_instances_count.InSyncStackInstancesCount"
    ]
    """<p>The number of stack instances which match the expected template and parameter configuration of the StackSet.</p>"""
    in_progress_stack_instances_count: NotRequired[
        "capo_cloudformation.types.in_progress_stack_instances_count.InProgressStackInstancesCount"
    ]
    """<p>The number of stack instances that are currently being checked for drift.</p>"""
    failed_stack_instances_count: NotRequired[
        "capo_cloudformation.types.failed_stack_instances_count.FailedStackInstancesCount"
    ]
    """<p>The number of stack instances for which the drift detection operation failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetDriftDetectionDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "drift_status" in value:
        import capo_cloudformation.types.stack_set_drift_status

        capo_cloudformation.types.stack_set_drift_status.serialize_query(
            value["drift_status"], pairs, f"{key_prefix}DriftStatus"
        )
    if "drift_detection_status" in value:
        import capo_cloudformation.types.stack_set_drift_detection_status

        capo_cloudformation.types.stack_set_drift_detection_status.serialize_query(
            value["drift_detection_status"], pairs, f"{key_prefix}DriftDetectionStatus"
        )
    if "last_drift_check_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_drift_check_timestamp"],
            pairs,
            f"{key_prefix}LastDriftCheckTimestamp",
        )
    if "total_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}TotalStackInstancesCount",
                str(value["total_stack_instances_count"]),
            )
        )
    if "drifted_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}DriftedStackInstancesCount",
                str(value["drifted_stack_instances_count"]),
            )
        )
    if "in_sync_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}InSyncStackInstancesCount",
                str(value["in_sync_stack_instances_count"]),
            )
        )
    if "in_progress_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}InProgressStackInstancesCount",
                str(value["in_progress_stack_instances_count"]),
            )
        )
    if "failed_stack_instances_count" in value:
        pairs.append(
            (
                f"{key_prefix}FailedStackInstancesCount",
                str(value["failed_stack_instances_count"]),
            )
        )


def deserialize_query(el: Element) -> StackSetDriftDetectionDetails:
    out: StackSetDriftDetectionDetails = {}  # type: ignore[typeddict-item]
    child_drift_status = el.find("DriftStatus")
    if child_drift_status is not None:
        import capo_cloudformation.types.stack_set_drift_status

        out["drift_status"] = (
            capo_cloudformation.types.stack_set_drift_status.deserialize_query(
                child_drift_status
            )
        )
    child_drift_detection_status = el.find("DriftDetectionStatus")
    if child_drift_detection_status is not None:
        import capo_cloudformation.types.stack_set_drift_detection_status

        out["drift_detection_status"] = (
            capo_cloudformation.types.stack_set_drift_detection_status.deserialize_query(
                child_drift_detection_status
            )
        )
    child_last_drift_check_timestamp = el.find("LastDriftCheckTimestamp")
    if child_last_drift_check_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["last_drift_check_timestamp"] = (
            capo_cloudformation.types.timestamp.deserialize_query(
                child_last_drift_check_timestamp
            )
        )
    child_total_stack_instances_count = el.find("TotalStackInstancesCount")
    if child_total_stack_instances_count is not None:
        out["total_stack_instances_count"] = int(
            child_total_stack_instances_count.text or ""
        )
    child_drifted_stack_instances_count = el.find("DriftedStackInstancesCount")
    if child_drifted_stack_instances_count is not None:
        out["drifted_stack_instances_count"] = int(
            child_drifted_stack_instances_count.text or ""
        )
    child_in_sync_stack_instances_count = el.find("InSyncStackInstancesCount")
    if child_in_sync_stack_instances_count is not None:
        out["in_sync_stack_instances_count"] = int(
            child_in_sync_stack_instances_count.text or ""
        )
    child_in_progress_stack_instances_count = el.find("InProgressStackInstancesCount")
    if child_in_progress_stack_instances_count is not None:
        out["in_progress_stack_instances_count"] = int(
            child_in_progress_stack_instances_count.text or ""
        )
    child_failed_stack_instances_count = el.find("FailedStackInstancesCount")
    if child_failed_stack_instances_count is not None:
        out["failed_stack_instances_count"] = int(
            child_failed_stack_instances_count.text or ""
        )
    return out
