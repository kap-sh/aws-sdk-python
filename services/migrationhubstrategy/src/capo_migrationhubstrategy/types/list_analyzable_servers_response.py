"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListAnalyzableServersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.analyzable_server_summary_list
    import capo_migrationhubstrategy.types.next_token


class ListAnalyzableServersResponse(TypedDict, closed=True):
    analyzable_servers: NotRequired[
        "capo_migrationhubstrategy.types.analyzable_server_summary_list.AnalyzableServerSummaryList"
    ]
    """The list of analyzable servers with summary information about each server."""
    next_token: NotRequired["capo_migrationhubstrategy.types.next_token.NextToken"]
    """The token you use to retrieve the next set of results, or null if there are no more results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyzableServersResponse) -> dict:
    out: dict = {}
    if "analyzable_servers" in value:
        import capo_migrationhubstrategy.types.analyzable_server_summary_list

        out["analyzableServers"] = (
            capo_migrationhubstrategy.types.analyzable_server_summary_list.serialize_json(
                value["analyzable_servers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnalyzableServersResponse:
    out: ListAnalyzableServersResponse = {}  # type: ignore[typeddict-item]
    if "analyzableServers" in data:
        import capo_migrationhubstrategy.types.analyzable_server_summary_list

        out["analyzable_servers"] = (
            capo_migrationhubstrategy.types.analyzable_server_summary_list.deserialize_json(
                data["analyzableServers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
