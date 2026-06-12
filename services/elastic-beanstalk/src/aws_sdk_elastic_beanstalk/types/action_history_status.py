"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ActionHistoryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

ActionHistoryStatus: TypeAlias = Literal[
    "Completed",
    "Failed",
    "Unknown",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Completed",
        "Failed",
        "Unknown",
    )
)


def to_query_text(value: ActionHistoryStatus) -> str:
    return value


def from_query_text(text: str) -> ActionHistoryStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ActionHistoryStatus value: {text!r}")
    return cast(ActionHistoryStatus, text)


def serialize_query(
    value: ActionHistoryStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActionHistoryStatus:
    return from_query_text(el.text or "")
