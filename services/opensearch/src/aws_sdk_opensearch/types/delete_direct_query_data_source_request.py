"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteDirectQueryDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.direct_query_data_source_name


class DeleteDirectQueryDataSourceRequest(TypedDict, closed=True):
    data_source_name: "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName"
    """<p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDirectQueryDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDirectQueryDataSourceRequest:
    out: DeleteDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
