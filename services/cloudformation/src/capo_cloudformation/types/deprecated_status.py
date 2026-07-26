"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeprecatedStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

DeprecatedStatus: TypeAlias = Literal[
    "LIVE",
    "DEPRECATED",
]


# --- awsQuery ser/de ---
def to_query_text(value: DeprecatedStatus) -> str:
    return value


def from_query_text(text: str) -> DeprecatedStatus:
    return cast(DeprecatedStatus, text)


def serialize_query(
    value: DeprecatedStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeprecatedStatus:
    return from_query_text(el.text or "")
