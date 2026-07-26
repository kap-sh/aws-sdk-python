"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.automation_event_filter_list
    import capo_compute_optimizer_automation.types.next_token


class ListAutomationEventsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_compute_optimizer_automation.types.automation_event_filter_list.AutomationEventFilterList"
    ]
    """<p> The filters to apply to the list of automation events. </p>"""
    start_time_inclusive: NotRequired["datetime.datetime"]
    """<p> The start of the time range to query for events. </p>"""
    end_time_exclusive: NotRequired["datetime.datetime"]
    """<p> The end of the time range to query for events. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of results to return in a single call. </p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p> The token for the next page of results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationEventsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_compute_optimizer_automation.types.automation_event_filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.automation_event_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "start_time_inclusive" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["startTimeInclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_time_inclusive"]
            )
        )
    if "end_time_exclusive" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["endTimeExclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_time_exclusive"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationEventsRequest:
    out: ListAutomationEventsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_compute_optimizer_automation.types.automation_event_filter_list

        out["filters"] = (
            capo_compute_optimizer_automation.types.automation_event_filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "startTimeInclusive" in data:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["start_time_inclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTimeInclusive"]
            )
        )
    if "endTimeExclusive" in data:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["end_time_exclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTimeExclusive"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
