"""Generated from Smithy shape ``com.amazonaws.appsync#ListDataSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.data_sources
    import capo_appsync.types.pagination_token


class ListDataSourcesResponse(TypedDict, closed=True):
    data_sources: NotRequired["capo_appsync.types.data_sources.DataSources"]
    """<p>The <code>DataSource</code> objects.</p>"""
    next_token: NotRequired["capo_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier to pass in the next request to this operation to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesResponse) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import capo_appsync.types.data_sources

        out["dataSources"] = capo_appsync.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSourcesResponse:
    out: ListDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "dataSources" in data:
        import capo_appsync.types.data_sources

        out["data_sources"] = capo_appsync.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
