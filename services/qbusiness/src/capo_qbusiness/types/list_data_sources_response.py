"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_sources
    import capo_qbusiness.types.next_token


class ListDataSourcesResponse(TypedDict, closed=True):
    data_sources: NotRequired["capo_qbusiness.types.data_sources.DataSources"]
    """<p>An array of summary information for one or more data source connector.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token. You can use this token in a subsequent request to retrieve the next set of data source connectors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesResponse) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import capo_qbusiness.types.data_sources

        out["dataSources"] = capo_qbusiness.types.data_sources.serialize_json(
            value["data_sources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSourcesResponse:
    out: ListDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "dataSources" in data:
        import capo_qbusiness.types.data_sources

        out["data_sources"] = capo_qbusiness.types.data_sources.deserialize_json(
            data["dataSources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
