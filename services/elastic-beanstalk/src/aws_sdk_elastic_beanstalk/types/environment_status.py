"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

EnvironmentStatus: TypeAlias = Literal[
    "Aborting",
    "Launching",
    "Updating",
    "LinkingFrom",
    "LinkingTo",
    "Ready",
    "Terminating",
    "Terminated",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Aborting",
        "Launching",
        "Updating",
        "LinkingFrom",
        "LinkingTo",
        "Ready",
        "Terminating",
        "Terminated",
    )
)


def to_query_text(value: EnvironmentStatus) -> str:
    return value


def from_query_text(text: str) -> EnvironmentStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentStatus value: {text!r}")
    return cast(EnvironmentStatus, text)


def serialize_query(
    value: EnvironmentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentStatus:
    return from_query_text(el.text or "")
