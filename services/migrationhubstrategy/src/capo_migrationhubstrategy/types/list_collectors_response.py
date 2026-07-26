"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListCollectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.collectors
    import capo_migrationhubstrategy.types.next_token


class ListCollectorsResponse(TypedDict, closed=True):
    collectors: NotRequired["capo_migrationhubstrategy.types.collectors.Collectors"]
    """<p> The list of all the installed collectors. </p>"""
    next_token: NotRequired["capo_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token you use to retrieve the next set of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollectorsResponse) -> dict:
    out: dict = {}
    if "collectors" in value:
        import capo_migrationhubstrategy.types.collectors

        out["Collectors"] = capo_migrationhubstrategy.types.collectors.serialize_json(
            value["collectors"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCollectorsResponse:
    out: ListCollectorsResponse = {}  # type: ignore[typeddict-item]
    if "Collectors" in data:
        import capo_migrationhubstrategy.types.collectors

        out["collectors"] = capo_migrationhubstrategy.types.collectors.deserialize_json(
            data["Collectors"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
