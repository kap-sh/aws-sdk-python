"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDirectQueryDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.direct_query_data_source_name


class GetDirectQueryDataSourceRequest(TypedDict, closed=True):
    data_source_name: (
        "capo_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName"
    )
    """<p> A unique, user-defined label that identifies the data source within your OpenSearch Service environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectQueryDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDirectQueryDataSourceRequest:
    out: GetDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
