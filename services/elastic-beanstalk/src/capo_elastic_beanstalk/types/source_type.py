"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SourceType``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

SourceType: TypeAlias = Literal[
    "Git",
    "Zip",
]


# --- awsQuery ser/de ---
def to_query_text(value: SourceType) -> str:
    return value


def from_query_text(text: str) -> SourceType:
    return cast(SourceType, text)


def serialize_query(
    value: SourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceType:
    return from_query_text(el.text or "")
