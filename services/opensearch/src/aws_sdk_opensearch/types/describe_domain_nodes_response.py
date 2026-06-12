"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainNodesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_nodes_status_list


class DescribeDomainNodesResponse(TypedDict):
    domain_nodes_status_list: NotRequired[
        "aws_sdk_opensearch.types.domain_nodes_status_list.DomainNodesStatusList"
    ]
    """<p>Contains nodes information list <code>DomainNodesStatusList</code> with details about the all nodes on the requested domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainNodesResponse) -> dict:
    out: dict = {}
    if "domain_nodes_status_list" in value:
        import aws_sdk_opensearch.types.domain_nodes_status_list

        out["DomainNodesStatusList"] = (
            aws_sdk_opensearch.types.domain_nodes_status_list.serialize_json(
                value["domain_nodes_status_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainNodesResponse:
    out: DescribeDomainNodesResponse = {}  # type: ignore[typeddict-item]
    if "DomainNodesStatusList" in data:
        import aws_sdk_opensearch.types.domain_nodes_status_list

        out["domain_nodes_status_list"] = (
            aws_sdk_opensearch.types.domain_nodes_status_list.deserialize_json(
                data["DomainNodesStatusList"]
            )
        )
    return out
