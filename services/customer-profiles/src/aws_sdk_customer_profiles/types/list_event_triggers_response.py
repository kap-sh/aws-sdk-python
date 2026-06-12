"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListEventTriggersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_summary_list
    import aws_sdk_customer_profiles.types.token


class ListEventTriggersResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_customer_profiles.types.event_trigger_summary_list.EventTriggerSummaryList"
    ]
    """<p>The list of Event Triggers.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListEventTriggers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventTriggersResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.event_trigger_summary_list

        out["Items"] = (
            aws_sdk_customer_profiles.types.event_trigger_summary_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventTriggersResponse:
    out: ListEventTriggersResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.event_trigger_summary_list

        out["items"] = (
            aws_sdk_customer_profiles.types.event_trigger_summary_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
