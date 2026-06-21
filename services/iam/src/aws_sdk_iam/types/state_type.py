"""Generated from Smithy shape ``com.amazonaws.iam#stateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

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
def to_query_text(value: stateType) -> str:
    return value


def from_query_text(text: str) -> stateType:
    return cast(stateType, text)


def serialize_query(
    value: stateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> stateType:
    return from_query_text(el.text or "")
