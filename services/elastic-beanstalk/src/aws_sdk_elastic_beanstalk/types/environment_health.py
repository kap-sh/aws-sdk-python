"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentHealth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

EnvironmentHealth: TypeAlias = Literal[
    "Green",
    "Yellow",
    "Red",
    "Grey",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Green",
        "Yellow",
        "Red",
        "Grey",
    )
)


def to_query_text(value: EnvironmentHealth) -> str:
    return value


def from_query_text(text: str) -> EnvironmentHealth:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentHealth value: {text!r}")
    return cast(EnvironmentHealth, text)


def serialize_query(
    value: EnvironmentHealth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentHealth:
    return from_query_text(el.text or "")
