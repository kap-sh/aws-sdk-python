"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListServersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.next_token
    import capo_migrationhubstrategy.types.server_details


class ListServersResponse(TypedDict, closed=True):
    server_infos: NotRequired[
        "capo_migrationhubstrategy.types.server_details.ServerDetails"
    ]
    """<p> The list of servers with detailed information about each server. </p>"""
    next_token: NotRequired["capo_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token you use to retrieve the next set of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServersResponse) -> dict:
    out: dict = {}
    if "server_infos" in value:
        import capo_migrationhubstrategy.types.server_details

        out["serverInfos"] = (
            capo_migrationhubstrategy.types.server_details.serialize_json(
                value["server_infos"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServersResponse:
    out: ListServersResponse = {}  # type: ignore[typeddict-item]
    if "serverInfos" in data:
        import capo_migrationhubstrategy.types.server_details

        out["server_infos"] = (
            capo_migrationhubstrategy.types.server_details.deserialize_json(
                data["serverInfos"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
