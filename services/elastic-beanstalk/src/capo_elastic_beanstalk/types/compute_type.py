"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ComputeType``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

ComputeType: TypeAlias = Literal[
    "BUILD_GENERAL1_SMALL",
    "BUILD_GENERAL1_MEDIUM",
    "BUILD_GENERAL1_LARGE",
]


# --- awsQuery ser/de ---
def to_query_text(value: ComputeType) -> str:
    return value


def from_query_text(text: str) -> ComputeType:
    return cast(ComputeType, text)


def serialize_query(
    value: ComputeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ComputeType:
    return from_query_text(el.text or "")
