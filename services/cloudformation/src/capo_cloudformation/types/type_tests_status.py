"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeTestsStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

TypeTestsStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "IN_PROGRESS",
    "NOT_TESTED",
]


# --- awsQuery ser/de ---
def to_query_text(value: TypeTestsStatus) -> str:
    return value


def from_query_text(text: str) -> TypeTestsStatus:
    return cast(TypeTestsStatus, text)


def serialize_query(
    value: TypeTestsStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TypeTestsStatus:
    return from_query_text(el.text or "")
