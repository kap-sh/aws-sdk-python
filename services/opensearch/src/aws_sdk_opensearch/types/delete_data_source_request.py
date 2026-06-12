"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteDataSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.data_source_name
    import aws_sdk_opensearch.types.domain_name


class DeleteDataSourceRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    name: "aws_sdk_opensearch.types.data_source_name.DataSourceName"
    """<p>The name of the data source to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSourceRequest:
    out: DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
    return out
