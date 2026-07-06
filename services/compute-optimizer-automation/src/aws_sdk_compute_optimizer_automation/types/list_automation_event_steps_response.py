"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.automation_event_steps
    import aws_sdk_compute_optimizer_automation.types.next_token


class ListAutomationEventStepsResponse(TypedDict, closed=True):
    automation_event_steps: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.automation_event_steps.AutomationEventSteps"
    ]
    """<p> The list of steps for the specified automation event. </p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventStepsResponse) -> dict:
    out: dict = {}
    if "automation_event_steps" in value:
        import aws_sdk_compute_optimizer_automation.types.automation_event_steps

        out["automationEventSteps"] = (
            aws_sdk_compute_optimizer_automation.types.automation_event_steps.serialize_aws_json_1_0(
                value["automation_event_steps"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventStepsResponse:
    out: ListAutomationEventStepsResponse = {}  # type: ignore[typeddict-item]
    if "automationEventSteps" in data:
        import aws_sdk_compute_optimizer_automation.types.automation_event_steps

        out["automation_event_steps"] = (
            aws_sdk_compute_optimizer_automation.types.automation_event_steps.deserialize_aws_json_1_0(
                data["automationEventSteps"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
