"""Generated from Smithy shape ``com.amazonaws.cloudformation#OnStackFailure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

OnStackFailure: TypeAlias = Literal[
    "DO_NOTHING",
    "ROLLBACK",
    "DELETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: OnStackFailure) -> str:
    return value


def from_query_text(text: str) -> OnStackFailure:
    return cast(OnStackFailure, text)


def serialize_query(
    value: OnStackFailure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OnStackFailure:
    return from_query_text(el.text or "")
