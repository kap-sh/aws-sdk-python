"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationEventSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.automation_event_summary

AutomationEventSummaryList: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.automation_event_summary.AutomationEventSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationEventSummaryList) -> list:
    import aws_sdk_compute_optimizer_automation.types.automation_event_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.automation_event_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutomationEventSummaryList:
    import aws_sdk_compute_optimizer_automation.types.automation_event_summary

    out: AutomationEventSummaryList = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.automation_event_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
