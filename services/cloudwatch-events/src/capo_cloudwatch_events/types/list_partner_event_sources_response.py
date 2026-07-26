"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListPartnerEventSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.next_token
    import capo_cloudwatch_events.types.partner_event_source_list


class ListPartnerEventSourcesResponse(TypedDict, closed=True):
    partner_event_sources: NotRequired[
        "capo_cloudwatch_events.types.partner_event_source_list.PartnerEventSourceList"
    ]
    """<p>The list of partner event sources returned by the operation.</p>"""
    next_token: NotRequired["capo_cloudwatch_events.types.next_token.NextToken"]
    """<p>A token you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerEventSourcesResponse) -> dict:
    out: dict = {}
    if "partner_event_sources" in value:
        import capo_cloudwatch_events.types.partner_event_source_list

        out["PartnerEventSources"] = (
            capo_cloudwatch_events.types.partner_event_source_list.serialize_aws_json_1_1(
                value["partner_event_sources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerEventSourcesResponse:
    out: ListPartnerEventSourcesResponse = {}  # type: ignore[typeddict-item]
    if "PartnerEventSources" in data:
        import capo_cloudwatch_events.types.partner_event_source_list

        out["partner_event_sources"] = (
            capo_cloudwatch_events.types.partner_event_source_list.deserialize_aws_json_1_1(
                data["PartnerEventSources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
