"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListPartnerEventSourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.next_token
    import aws_sdk_eventbridge.types.partner_event_source_list


class ListPartnerEventSourcesResponse(TypedDict):
    partner_event_sources: NotRequired[
        "aws_sdk_eventbridge.types.partner_event_source_list.PartnerEventSourceList"
    ]
    """<p>The list of partner event sources returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerEventSourcesResponse) -> dict:
    out: dict = {}
    if "partner_event_sources" in value:
        import aws_sdk_eventbridge.types.partner_event_source_list

        out["PartnerEventSources"] = (
            aws_sdk_eventbridge.types.partner_event_source_list.serialize_aws_json_1_1(
                value["partner_event_sources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerEventSourcesResponse:
    out: ListPartnerEventSourcesResponse = {}  # type: ignore[typeddict-item]
    if "PartnerEventSources" in data:
        import aws_sdk_eventbridge.types.partner_event_source_list

        out["partner_event_sources"] = (
            aws_sdk_eventbridge.types.partner_event_source_list.deserialize_aws_json_1_1(
                data["PartnerEventSources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
