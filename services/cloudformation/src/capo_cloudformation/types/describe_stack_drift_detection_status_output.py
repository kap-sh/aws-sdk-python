"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackDriftDetectionStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.boxed_integer
    import capo_cloudformation.types.stack_drift_detection_id
    import capo_cloudformation.types.stack_drift_detection_status
    import capo_cloudformation.types.stack_drift_detection_status_reason
    import capo_cloudformation.types.stack_drift_status
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.timestamp


class DescribeStackDriftDetectionStatusOutput(TypedDict, closed=True):
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The ID of the stack.</p>"""
    stack_drift_detection_id: NotRequired[
        "capo_cloudformation.types.stack_drift_detection_id.StackDriftDetectionId"
    ]
    """<p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of reports CloudFormation retains for any given stack, and for how long, may vary.</p>"""
    stack_drift_status: NotRequired[
        "capo_cloudformation.types.stack_drift_status.StackDriftStatus"
    ]
    """<p>Status of the stack's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack differs from its expected template configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: CloudFormation could not run drift detection for a resource in the stack. See the <code>DetectionStatusReason</code> for details.</p> </li> </ul>"""
    detection_status: NotRequired[
        "capo_cloudformation.types.stack_drift_detection_status.StackDriftDetectionStatus"
    ]
    """<p>The status of the stack drift detection operation.</p> <ul> <li> <p> <code>DETECTION_COMPLETE</code>: The stack drift detection operation has successfully completed for all resources in the stack that support drift detection. (Resources that don't currently support stack detection remain unchecked.)</p> <p>If you specified logical resource IDs for CloudFormation to use as a filter for the stack drift detection operation, only the resources with those logical IDs are checked for drift.</p> </li> <li> <p> <code>DETECTION_FAILED</code>: The stack drift detection operation has failed for at least one resource in the stack. Results will be available for resources on which CloudFormation successfully completed drift detection.</p> </li> <li> <p> <code>DETECTION_IN_PROGRESS</code>: The stack drift detection operation is currently in progress.</p> </li> </ul>"""
    detection_status_reason: NotRequired[
        "capo_cloudformation.types.stack_drift_detection_status_reason.StackDriftDetectionStatusReason"
    ]
    """<p>The reason the stack drift detection operation has its current status.</p>"""
    drifted_stack_resource_count: NotRequired[
        "capo_cloudformation.types.boxed_integer.BoxedInteger"
    ]
    """<p>Total number of stack resources that have drifted. This is NULL until the drift detection operation reaches a status of <code>DETECTION_COMPLETE</code>. This value will be 0 for stacks whose drift status is <code>IN_SYNC</code>.</p>"""
    timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>Time at which the stack drift detection operation was initiated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackDriftDetectionStatusOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "stack_drift_detection_id" in value:
        pairs.append(
            (
                f"{key_prefix}StackDriftDetectionId",
                str(value["stack_drift_detection_id"]),
            )
        )
    if "stack_drift_status" in value:
        import capo_cloudformation.types.stack_drift_status

        capo_cloudformation.types.stack_drift_status.serialize_query(
            value["stack_drift_status"], pairs, f"{key_prefix}StackDriftStatus"
        )
    if "detection_status" in value:
        import capo_cloudformation.types.stack_drift_detection_status

        capo_cloudformation.types.stack_drift_detection_status.serialize_query(
            value["detection_status"], pairs, f"{key_prefix}DetectionStatus"
        )
    if "detection_status_reason" in value:
        pairs.append(
            (
                f"{key_prefix}DetectionStatusReason",
                str(value["detection_status_reason"]),
            )
        )
    if "drifted_stack_resource_count" in value:
        pairs.append(
            (
                f"{key_prefix}DriftedStackResourceCount",
                str(value["drifted_stack_resource_count"]),
            )
        )
    if "timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )


def deserialize_query(el: Element) -> DescribeStackDriftDetectionStatusOutput:
    out: DescribeStackDriftDetectionStatusOutput = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_stack_drift_detection_id = el.find("StackDriftDetectionId")
    if child_stack_drift_detection_id is not None:
        out["stack_drift_detection_id"] = str(child_stack_drift_detection_id.text or "")
    child_stack_drift_status = el.find("StackDriftStatus")
    if child_stack_drift_status is not None:
        import capo_cloudformation.types.stack_drift_status

        out["stack_drift_status"] = (
            capo_cloudformation.types.stack_drift_status.deserialize_query(
                child_stack_drift_status
            )
        )
    child_detection_status = el.find("DetectionStatus")
    if child_detection_status is not None:
        import capo_cloudformation.types.stack_drift_detection_status

        out["detection_status"] = (
            capo_cloudformation.types.stack_drift_detection_status.deserialize_query(
                child_detection_status
            )
        )
    child_detection_status_reason = el.find("DetectionStatusReason")
    if child_detection_status_reason is not None:
        out["detection_status_reason"] = str(child_detection_status_reason.text or "")
    child_drifted_stack_resource_count = el.find("DriftedStackResourceCount")
    if child_drifted_stack_resource_count is not None:
        out["drifted_stack_resource_count"] = int(
            child_drifted_stack_resource_count.text or ""
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["timestamp"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_timestamp
        )
    return out
