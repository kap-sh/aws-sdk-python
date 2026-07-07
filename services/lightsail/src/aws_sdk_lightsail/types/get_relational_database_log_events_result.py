"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseLogEventsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.log_event_list
    import aws_sdk_lightsail.types.string


class GetRelationalDatabaseLogEventsResult(TypedDict, closed=True):
    resource_log_events: NotRequired[
        "aws_sdk_lightsail.types.log_event_list.LogEventList"
    ]
    """<p>An object describing the result of your get relational database log events request.</p>"""
    next_backward_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>A token used for advancing to the previous page of results from your get relational database log events request.</p>"""
    next_forward_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>A token used for advancing to the next page of results from your get relational database log events request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseLogEventsResult) -> dict:
    out: dict = {}
    if "resource_log_events" in value:
        import aws_sdk_lightsail.types.log_event_list

        out["resourceLogEvents"] = (
            aws_sdk_lightsail.types.log_event_list.serialize_aws_json_1_1(
                value["resource_log_events"]
            )
        )
    if "next_backward_token" in value:
        out["nextBackwardToken"] = value["next_backward_token"]
    if "next_forward_token" in value:
        out["nextForwardToken"] = value["next_forward_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseLogEventsResult:
    out: GetRelationalDatabaseLogEventsResult = {}  # type: ignore[typeddict-item]
    if "resourceLogEvents" in data:
        import aws_sdk_lightsail.types.log_event_list

        out["resource_log_events"] = (
            aws_sdk_lightsail.types.log_event_list.deserialize_aws_json_1_1(
                data["resourceLogEvents"]
            )
        )
    if "nextBackwardToken" in data:
        out["next_backward_token"] = data["nextBackwardToken"]
    if "nextForwardToken" in data:
        out["next_forward_token"] = data["nextForwardToken"]
    return out
