"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseEventsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_event_list
    import capo_lightsail.types.string


class GetRelationalDatabaseEventsResult(TypedDict, closed=True):
    relational_database_events: NotRequired[
        "capo_lightsail.types.relational_database_event_list.RelationalDatabaseEventList"
    ]
    """<p>An object describing the result of your get relational database events request.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetRelationalDatabaseEvents</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseEventsResult) -> dict:
    out: dict = {}
    if "relational_database_events" in value:
        import capo_lightsail.types.relational_database_event_list

        out["relationalDatabaseEvents"] = (
            capo_lightsail.types.relational_database_event_list.serialize_aws_json_1_1(
                value["relational_database_events"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseEventsResult:
    out: GetRelationalDatabaseEventsResult = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseEvents" in data:
        import capo_lightsail.types.relational_database_event_list

        out["relational_database_events"] = (
            capo_lightsail.types.relational_database_event_list.deserialize_aws_json_1_1(
                data["relationalDatabaseEvents"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
