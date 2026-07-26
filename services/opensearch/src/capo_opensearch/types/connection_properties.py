"""Generated from Smithy shape ``com.amazonaws.opensearch#ConnectionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cross_cluster_search_connection_properties
    import capo_opensearch.types.endpoint


class ConnectionProperties(TypedDict, closed=True):
    endpoint: NotRequired["capo_opensearch.types.endpoint.Endpoint"]
    """<important> <p>The Endpoint attribute cannot be modified. </p> </important> <p>The endpoint of the remote domain. Applicable for VPC_ENDPOINT connection mode.</p>"""
    cross_cluster_search: NotRequired[
        "capo_opensearch.types.cross_cluster_search_connection_properties.CrossClusterSearchConnectionProperties"
    ]
    """<p>The connection properties for cross cluster search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionProperties) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "cross_cluster_search" in value:
        import capo_opensearch.types.cross_cluster_search_connection_properties

        out["CrossClusterSearch"] = (
            capo_opensearch.types.cross_cluster_search_connection_properties.serialize_json(
                value["cross_cluster_search"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectionProperties:
    out: ConnectionProperties = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "CrossClusterSearch" in data:
        import capo_opensearch.types.cross_cluster_search_connection_properties

        out["cross_cluster_search"] = (
            capo_opensearch.types.cross_cluster_search_connection_properties.deserialize_json(
                data["CrossClusterSearch"]
            )
        )
    return out
