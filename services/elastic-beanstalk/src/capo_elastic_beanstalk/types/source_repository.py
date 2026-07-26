"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SourceRepository``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

SourceRepository: TypeAlias = Literal[
    "CodeCommit",
    "S3",
]


# --- awsQuery ser/de ---
def to_query_text(value: SourceRepository) -> str:
    return value


def from_query_text(text: str) -> SourceRepository:
    return cast(SourceRepository, text)


def serialize_query(
    value: SourceRepository, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceRepository:
    return from_query_text(el.text or "")
