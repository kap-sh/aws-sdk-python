"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.lifecycle_execution_id
    import capo_imagebuilder.types.lifecycle_execution_resources_impacted_summary
    import capo_imagebuilder.types.lifecycle_execution_state
    import capo_imagebuilder.types.lifecycle_policy_arn


class LifecycleExecution(TypedDict, closed=True):
    lifecycle_execution_id: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    ]
    """<p>Identifies the lifecycle policy runtime instance.</p>"""
    lifecycle_policy_arn: NotRequired[
        "capo_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy that ran.</p>"""
    resources_impacted_summary: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_resources_impacted_summary.LifecycleExecutionResourcesImpactedSummary"
    ]
    """<p>Contains information about associated resources that are identified for action by the runtime instance of the lifecycle policy.</p>"""
    state: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_state.LifecycleExecutionState"
    ]
    """<p>Runtime state that reports if the policy action ran successfully, failed, or was skipped.</p>"""
    start_time: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when the lifecycle runtime instance started.</p>"""
    end_time: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp when the lifecycle runtime instance completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecution) -> dict:
    out: dict = {}
    if "lifecycle_execution_id" in value:
        out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
    if "lifecycle_policy_arn" in value:
        out["lifecyclePolicyArn"] = value["lifecycle_policy_arn"]
    if "resources_impacted_summary" in value:
        import capo_imagebuilder.types.lifecycle_execution_resources_impacted_summary

        out["resourcesImpactedSummary"] = (
            capo_imagebuilder.types.lifecycle_execution_resources_impacted_summary.serialize_json(
                value["resources_impacted_summary"]
            )
        )
    if "state" in value:
        import capo_imagebuilder.types.lifecycle_execution_state

        out["state"] = capo_imagebuilder.types.lifecycle_execution_state.serialize_json(
            value["state"]
        )
    if "start_time" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["startTime"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["endTime"] = capo_imagebuilder.types.date_time_timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> LifecycleExecution:
    out: LifecycleExecution = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutionId" in data:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
    if "lifecyclePolicyArn" in data:
        out["lifecycle_policy_arn"] = data["lifecyclePolicyArn"]
    if "resourcesImpactedSummary" in data:
        import capo_imagebuilder.types.lifecycle_execution_resources_impacted_summary

        out["resources_impacted_summary"] = (
            capo_imagebuilder.types.lifecycle_execution_resources_impacted_summary.deserialize_json(
                data["resourcesImpactedSummary"]
            )
        )
    if "state" in data:
        import capo_imagebuilder.types.lifecycle_execution_state

        out["state"] = (
            capo_imagebuilder.types.lifecycle_execution_state.deserialize_json(
                data["state"]
            )
        )
    if "startTime" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["start_time"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_imagebuilder.types.date_time_timestamp

        out["end_time"] = capo_imagebuilder.types.date_time_timestamp.deserialize_json(
            data["endTime"]
        )
    return out
