"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataLakeNamespacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_namespace_max_results
    import aws_sdk_supplychain.types.data_lake_namespace_next_token
    import aws_sdk_supplychain.types.uuid


class ListDataLakeNamespacesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    next_token: NotRequired[
        "aws_sdk_supplychain.types.data_lake_namespace_next_token.DataLakeNamespaceNextToken"
    ]
    """<p>The pagination token to fetch next page of namespaces.</p>"""
    max_results: "aws_sdk_supplychain.types.data_lake_namespace_max_results.DataLakeNamespaceMaxResults"
    """<p>The max number of namespaces to fetch in this paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeNamespacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataLakeNamespacesRequest:
    out: ListDataLakeNamespacesRequest = {}  # type: ignore[typeddict-item]
    return out
