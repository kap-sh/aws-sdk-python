"""Generated from Smithy shape ``com.amazonaws.cloudformation#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ExecutionStatus: TypeAlias = Literal[
    "UNAVAILABLE",
    "AVAILABLE",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_COMPLETE",
    "EXECUTE_FAILED",
    "OBSOLETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: ExecutionStatus) -> str:
    return value


def from_query_text(text: str) -> ExecutionStatus:
    return cast(ExecutionStatus, text)


def serialize_query(
    value: ExecutionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ExecutionStatus:
    return from_query_text(el.text or "")
