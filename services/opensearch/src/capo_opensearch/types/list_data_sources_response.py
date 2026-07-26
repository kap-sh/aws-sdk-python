"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDataSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.data_source_list


class ListDataSourcesResponse(TypedDict, closed=True):
    data_sources: NotRequired["capo_opensearch.types.data_source_list.DataSourceList"]
    """<p>A list of data sources associated with specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesResponse) -> dict:
    out: dict = {}
    if "data_sources" in value:
        import capo_opensearch.types.data_source_list

        out["DataSources"] = capo_opensearch.types.data_source_list.serialize_json(
            value["data_sources"]
        )
    return out


def deserialize_json(data: dict) -> ListDataSourcesResponse:
    out: ListDataSourcesResponse = {}  # type: ignore[typeddict-item]
    if "DataSources" in data:
        import capo_opensearch.types.data_source_list

        out["data_sources"] = capo_opensearch.types.data_source_list.deserialize_json(
            data["DataSources"]
        )
    return out
