"""Generated from Smithy shape ``com.amazonaws.cloudformation#OnFailure``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

OnFailure: TypeAlias = Literal[
    "DO_NOTHING",
    "ROLLBACK",
    "DELETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: OnFailure) -> str:
    return value


def from_query_text(text: str) -> OnFailure:
    return cast(OnFailure, text)


def serialize_query(
    value: OnFailure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OnFailure:
    return from_query_text(el.text or "")
