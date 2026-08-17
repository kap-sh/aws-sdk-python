"""Generated from Smithy shape ``com.amazonaws.ssm#ListOpsItemEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_event_summaries
    import capo_ssm.types.string


class ListOpsItemEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm.types.string.String"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results. </p>"""
    summaries: NotRequired[
        "capo_ssm.types.ops_item_event_summaries.OpsItemEventSummaries"
    ]
    """<p>A list of event information for the specified OpsItems.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOpsItemEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "summaries" in value:
        import capo_ssm.types.ops_item_event_summaries

        out["Summaries"] = (
            capo_ssm.types.ops_item_event_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOpsItemEventsResponse:
    out: ListOpsItemEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Summaries") is not None:
        import capo_ssm.types.ops_item_event_summaries

        out["summaries"] = (
            capo_ssm.types.ops_item_event_summaries.deserialize_aws_json_1_1(
                data["Summaries"]
            )
        )
    return out
