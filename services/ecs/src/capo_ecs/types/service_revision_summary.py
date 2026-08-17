"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.double
    import capo_ecs.types.integer
    import capo_ecs.types.string


class ServiceRevisionSummary(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service revision.</p>"""
    requested_task_count: "capo_ecs.types.integer.Integer"
    """<p>The number of requested tasks for the service revision.</p>"""
    running_task_count: "capo_ecs.types.integer.Integer"
    """<p>The number of running tasks for the service revision.</p>"""
    pending_task_count: "capo_ecs.types.integer.Integer"
    """<p>The number of pending tasks for the service revision.</p>"""
    requested_test_traffic_weight: NotRequired["capo_ecs.types.double.Double"]
    """<p>The percentage of test traffic that is directed to this service revision. This value represents a snapshot of the traffic distribution and may not reflect real-time changes during active deployments. Valid values are 0.0 to 100.0.</p>"""
    requested_production_traffic_weight: NotRequired["capo_ecs.types.double.Double"]
    """<p>The percentage of production traffic that is directed to this service revision. This value represents a snapshot of the traffic distribution and may not reflect real-time changes during active deployments. Valid values are 0.0 to 100.0.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    out["requestedTaskCount"] = value.get("requested_task_count", 0)
    out["runningTaskCount"] = value.get("running_task_count", 0)
    out["pendingTaskCount"] = value.get("pending_task_count", 0)
    if "requested_test_traffic_weight" in value:
        out["requestedTestTrafficWeight"] = value["requested_test_traffic_weight"]
    if "requested_production_traffic_weight" in value:
        out["requestedProductionTrafficWeight"] = value[
            "requested_production_traffic_weight"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceRevisionSummary:
    out: ServiceRevisionSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("requestedTaskCount") is not None:
        out["requested_task_count"] = data["requestedTaskCount"]
    else:
        out["requested_task_count"] = 0
    if data.get("runningTaskCount") is not None:
        out["running_task_count"] = data["runningTaskCount"]
    else:
        out["running_task_count"] = 0
    if data.get("pendingTaskCount") is not None:
        out["pending_task_count"] = data["pendingTaskCount"]
    else:
        out["pending_task_count"] = 0
    if data.get("requestedTestTrafficWeight") is not None:
        out["requested_test_traffic_weight"] = data["requestedTestTrafficWeight"]
    if data.get("requestedProductionTrafficWeight") is not None:
        out["requested_production_traffic_weight"] = data[
            "requestedProductionTrafficWeight"
        ]
    return out
