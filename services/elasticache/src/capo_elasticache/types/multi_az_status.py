"""Generated from Smithy shape ``com.amazonaws.elasticache#MultiAZStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

MultiAZStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsQuery ser/de ---
def to_query_text(value: MultiAZStatus) -> str:
    return value


def from_query_text(text: str) -> MultiAZStatus:
    return cast(MultiAZStatus, text)


def serialize_query(
    value: MultiAZStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MultiAZStatus:
    return from_query_text(el.text or "")
