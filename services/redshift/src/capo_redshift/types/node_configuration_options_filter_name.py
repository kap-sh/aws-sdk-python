"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOptionsFilterName``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

NodeConfigurationOptionsFilterName: TypeAlias = Literal[
    "NodeType",
    "NumberOfNodes",
    "EstimatedDiskUtilizationPercent",
    "Mode",
]


# --- awsQuery ser/de ---
def to_query_text(value: NodeConfigurationOptionsFilterName) -> str:
    return value


def from_query_text(text: str) -> NodeConfigurationOptionsFilterName:
    return cast(NodeConfigurationOptionsFilterName, text)


def serialize_query(
    value: NodeConfigurationOptionsFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NodeConfigurationOptionsFilterName:
    return from_query_text(el.text or "")
