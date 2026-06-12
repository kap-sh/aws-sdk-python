"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentHealthAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

EnvironmentHealthAttribute: TypeAlias = Literal[
    "Status",
    "Color",
    "Causes",
    "ApplicationMetrics",
    "InstancesHealth",
    "All",
    "HealthStatus",
    "RefreshedAt",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Status",
        "Color",
        "Causes",
        "ApplicationMetrics",
        "InstancesHealth",
        "All",
        "HealthStatus",
        "RefreshedAt",
    )
)


def to_query_text(value: EnvironmentHealthAttribute) -> str:
    return value


def from_query_text(text: str) -> EnvironmentHealthAttribute:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown EnvironmentHealthAttribute value: {text!r}"
        )
    return cast(EnvironmentHealthAttribute, text)


def serialize_query(
    value: EnvironmentHealthAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentHealthAttribute:
    return from_query_text(el.text or "")
