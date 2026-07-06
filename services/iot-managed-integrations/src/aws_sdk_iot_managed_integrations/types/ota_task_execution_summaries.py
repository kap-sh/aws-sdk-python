"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionSummaries``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.ota_task_execution_summary


class OtaTaskExecutionSummaries(TypedDict, closed=True):
    task_execution_summary: NotRequired[
        "aws_sdk_iot_managed_integrations.types.ota_task_execution_summary.OtaTaskExecutionSummary"
    ]
    """<p>Structure representing one over-the-air (OTA) task execution summary</p>"""
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskExecutionSummaries) -> dict:
    out: dict = {}
    if "task_execution_summary" in value:
        import aws_sdk_iot_managed_integrations.types.ota_task_execution_summary

        out["TaskExecutionSummary"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_execution_summary.serialize_json(
                value["task_execution_summary"]
            )
        )
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    return out


def deserialize_json(data: dict) -> OtaTaskExecutionSummaries:
    out: OtaTaskExecutionSummaries = {}  # type: ignore[typeddict-item]
    if "TaskExecutionSummary" in data:
        import aws_sdk_iot_managed_integrations.types.ota_task_execution_summary

        out["task_execution_summary"] = (
            aws_sdk_iot_managed_integrations.types.ota_task_execution_summary.deserialize_json(
                data["TaskExecutionSummary"]
            )
        )
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    return out
