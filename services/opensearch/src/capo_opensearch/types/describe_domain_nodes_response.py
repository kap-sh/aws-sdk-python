"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_nodes_status_list


class DescribeDomainNodesResponse(TypedDict, closed=True):
    domain_nodes_status_list: NotRequired[
        "capo_opensearch.types.domain_nodes_status_list.DomainNodesStatusList"
    ]
    """<p>Contains nodes information list <code>DomainNodesStatusList</code> with details about the all nodes on the requested domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainNodesResponse) -> dict:
    out: dict = {}
    if "domain_nodes_status_list" in value:
        import capo_opensearch.types.domain_nodes_status_list

        out["DomainNodesStatusList"] = (
            capo_opensearch.types.domain_nodes_status_list.serialize_json(
                value["domain_nodes_status_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainNodesResponse:
    out: DescribeDomainNodesResponse = {}  # type: ignore[typeddict-item]
    if "DomainNodesStatusList" in data:
        import capo_opensearch.types.domain_nodes_status_list

        out["domain_nodes_status_list"] = (
            capo_opensearch.types.domain_nodes_status_list.deserialize_json(
                data["DomainNodesStatusList"]
            )
        )
    return out
