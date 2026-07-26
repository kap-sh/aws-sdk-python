"""Generated from Smithy shape ``com.amazonaws.cloudformation#CallAs``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

CallAs: TypeAlias = Literal[
    "SELF",
    "DELEGATED_ADMIN",
]


# --- awsQuery ser/de ---
def to_query_text(value: CallAs) -> str:
    return value


def from_query_text(text: str) -> CallAs:
    return cast(CallAs, text)


def serialize_query(value: CallAs, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CallAs:
    return from_query_text(el.text or "")
