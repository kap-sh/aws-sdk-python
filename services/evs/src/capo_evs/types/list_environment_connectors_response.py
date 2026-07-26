"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.connector_list
    import capo_evs.types.pagination_token


class ListEnvironmentConnectorsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    connectors: NotRequired["capo_evs.types.connector_list.ConnectorList"]
    """<p>A list of connectors in the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentConnectorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "connectors" in value:
        import capo_evs.types.connector_list

        out["connectors"] = capo_evs.types.connector_list.serialize_aws_json_1_0(
            value["connectors"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentConnectorsResponse:
    out: ListEnvironmentConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "connectors" in data:
        import capo_evs.types.connector_list

        out["connectors"] = capo_evs.types.connector_list.deserialize_aws_json_1_0(
            data["connectors"]
        )
    return out
