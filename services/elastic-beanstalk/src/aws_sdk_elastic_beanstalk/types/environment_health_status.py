"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentHealthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element

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
def to_query_text(value: EnvironmentHealthStatus) -> str:
    return value


def from_query_text(text: str) -> EnvironmentHealthStatus:
    return cast(EnvironmentHealthStatus, text)


def serialize_query(
    value: EnvironmentHealthStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentHealthStatus:
    return from_query_text(el.text or "")
