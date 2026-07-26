"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

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
def to_query_text(value: EnvironmentStatus) -> str:
    return value


def from_query_text(text: str) -> EnvironmentStatus:
    return cast(EnvironmentStatus, text)


def serialize_query(
    value: EnvironmentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentStatus:
    return from_query_text(el.text or "")
