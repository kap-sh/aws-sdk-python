"""Generated from Smithy shape ``com.amazonaws.rds#TargetConnectionNetworkType``."""

from typing import Literal, TypeAlias, cast

from capo_rds._protocol.xml import Element

TargetConnectionNetworkType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetConnectionNetworkType) -> str:
    return value


def from_query_text(text: str) -> TargetConnectionNetworkType:
    return cast(TargetConnectionNetworkType, text)


def serialize_query(
    value: TargetConnectionNetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetConnectionNetworkType:
    return from_query_text(el.text or "")
