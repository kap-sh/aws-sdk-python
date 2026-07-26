"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotInstanceRequestState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CancelSpotInstanceRequestState: TypeAlias = Literal[
    "active",
    "open",
    "closed",
    "cancelled",
    "completed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CancelSpotInstanceRequestState) -> str:
    return value


def from_ec2_query_text(text: str) -> CancelSpotInstanceRequestState:
    return cast(CancelSpotInstanceRequestState, text)


def serialize_ec2_query(
    value: CancelSpotInstanceRequestState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CancelSpotInstanceRequestState:
    return from_ec2_query_text(el.text or "")
