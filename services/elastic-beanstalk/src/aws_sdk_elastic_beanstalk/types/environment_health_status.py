"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentHealthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

EnvironmentHealthStatus: TypeAlias = Literal[
    "NoData",
    "Unknown",
    "Pending",
    "Ok",
    "Info",
    "Warning",
    "Degraded",
    "Severe",
    "Suspended",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoData",
        "Unknown",
        "Pending",
        "Ok",
        "Info",
        "Warning",
        "Degraded",
        "Severe",
        "Suspended",
    )
)


def to_query_text(value: EnvironmentHealthStatus) -> str:
    return value


def from_query_text(text: str) -> EnvironmentHealthStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentHealthStatus value: {text!r}")
    return cast(EnvironmentHealthStatus, text)


def serialize_query(
    value: EnvironmentHealthStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentHealthStatus:
    return from_query_text(el.text or "")
