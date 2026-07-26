"""Generated from Smithy shape ``com.amazonaws.appflow#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.connector_list
    import capo_appflow.types.next_token


class ListConnectorsResponse(TypedDict, closed=True):
    connectors: NotRequired["capo_appflow.types.connector_list.ConnectorList"]
    """<p>Contains information about the connectors supported by Amazon AppFlow.</p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p>The pagination token for the next page of data. If nextToken=null, this means that all records have been fetched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    if "connectors" in value:
        import capo_appflow.types.connector_list

        out["connectors"] = capo_appflow.types.connector_list.serialize_json(
            value["connectors"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "connectors" in data:
        import capo_appflow.types.connector_list

        out["connectors"] = capo_appflow.types.connector_list.deserialize_json(
            data["connectors"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
