"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOptionsFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

NodeConfigurationOptionsFilterName: TypeAlias = Literal[
    "NodeType",
    "NumberOfNodes",
    "EstimatedDiskUtilizationPercent",
    "Mode",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NodeType",
        "NumberOfNodes",
        "EstimatedDiskUtilizationPercent",
        "Mode",
    )
)


def to_query_text(value: NodeConfigurationOptionsFilterName) -> str:
    return value


def from_query_text(text: str) -> NodeConfigurationOptionsFilterName:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown NodeConfigurationOptionsFilterName value: {text!r}"
        )
    return cast(NodeConfigurationOptionsFilterName, text)


def serialize_query(
    value: NodeConfigurationOptionsFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NodeConfigurationOptionsFilterName:
    return from_query_text(el.text or "")
