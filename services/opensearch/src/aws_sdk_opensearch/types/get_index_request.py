"""Generated from Smithy shape ``com.amazonaws.opensearch#GetIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.index_name


class GetIndexRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    index_name: "aws_sdk_opensearch.types.index_name.IndexName"
    """<p>The name of the index to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIndexRequest:
    out: GetIndexRequest = {}  # type: ignore[typeddict-item]
    return out
