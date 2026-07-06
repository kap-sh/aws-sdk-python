"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.automation_events
    import aws_sdk_compute_optimizer_automation.types.next_token


class ListAutomationEventsResponse(TypedDict, closed=True):
    automation_events: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.automation_events.AutomationEvents"
    ]
    """<p> The list of automation events that match the specified criteria. </p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p> The token to use to retrieve the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventsResponse) -> dict:
    out: dict = {}
    if "automation_events" in value:
        import aws_sdk_compute_optimizer_automation.types.automation_events

        out["automationEvents"] = (
            aws_sdk_compute_optimizer_automation.types.automation_events.serialize_aws_json_1_0(
                value["automation_events"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventsResponse:
    out: ListAutomationEventsResponse = {}  # type: ignore[typeddict-item]
    if "automationEvents" in data:
        import aws_sdk_compute_optimizer_automation.types.automation_events

        out["automation_events"] = (
            aws_sdk_compute_optimizer_automation.types.automation_events.deserialize_aws_json_1_0(
                data["automationEvents"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
