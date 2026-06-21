"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentInfoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element

EnvironmentInfoType: TypeAlias = Literal[
    "tail",
    "bundle",
    "analyze",
]


# --- awsQuery ser/de ---
def to_query_text(value: EnvironmentInfoType) -> str:
    return value


def from_query_text(text: str) -> EnvironmentInfoType:
    return cast(EnvironmentInfoType, text)


def serialize_query(
    value: EnvironmentInfoType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentInfoType:
    return from_query_text(el.text or "")
