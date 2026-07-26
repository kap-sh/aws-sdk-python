"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainNodesStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.domain_nodes_status

DomainNodesStatusList: TypeAlias = list[
    "capo_opensearch.types.domain_nodes_status.DomainNodesStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNodesStatusList) -> list:
    import capo_opensearch.types.domain_nodes_status

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.domain_nodes_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainNodesStatusList:
    import capo_opensearch.types.domain_nodes_status

    out: DomainNodesStatusList = []
    for item in data:
        out.append(capo_opensearch.types.domain_nodes_status.deserialize_json(item))
    return out
