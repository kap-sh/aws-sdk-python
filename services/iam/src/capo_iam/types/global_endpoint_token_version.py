"""Generated from Smithy shape ``com.amazonaws.iam#globalEndpointTokenVersion``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

globalEndpointTokenVersion: TypeAlias = Literal[
    "v1Token",
    "v2Token",
]


# --- awsQuery ser/de ---
def to_query_text(value: globalEndpointTokenVersion) -> str:
    return value


def from_query_text(text: str) -> globalEndpointTokenVersion:
    return cast(globalEndpointTokenVersion, text)


def serialize_query(
    value: globalEndpointTokenVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> globalEndpointTokenVersion:
    return from_query_text(el.text or "")
