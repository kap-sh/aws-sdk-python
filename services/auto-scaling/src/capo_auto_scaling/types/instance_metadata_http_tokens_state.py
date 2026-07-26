"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceMetadataHttpTokensState``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

InstanceMetadataHttpTokensState: TypeAlias = Literal[
    "optional",
    "required",
]


# --- awsQuery ser/de ---
def to_query_text(value: InstanceMetadataHttpTokensState) -> str:
    return value


def from_query_text(text: str) -> InstanceMetadataHttpTokensState:
    return cast(InstanceMetadataHttpTokensState, text)


def serialize_query(
    value: InstanceMetadataHttpTokensState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InstanceMetadataHttpTokensState:
    return from_query_text(el.text or "")
