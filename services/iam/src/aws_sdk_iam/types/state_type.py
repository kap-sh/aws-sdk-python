"""Generated from Smithy shape ``com.amazonaws.iam#stateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

stateType: TypeAlias = Literal[
    "UNASSIGNED",
    "ASSIGNED",
    "PENDING_APPROVAL",
    "FINALIZED",
    "ACCEPTED",
    "REJECTED",
    "EXPIRED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNASSIGNED",
        "ASSIGNED",
        "PENDING_APPROVAL",
        "FINALIZED",
        "ACCEPTED",
        "REJECTED",
        "EXPIRED",
    )
)


def to_query_text(value: stateType) -> str:
    return value


def from_query_text(text: str) -> stateType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown stateType value: {text!r}")
    return cast(stateType, text)


def serialize_query(
    value: stateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> stateType:
    return from_query_text(el.text or "")
