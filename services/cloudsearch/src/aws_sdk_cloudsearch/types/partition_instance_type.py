"""Generated from Smithy shape ``com.amazonaws.cloudsearch#PartitionInstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudsearch._protocol.xml import Element

"""<p>The instance type (such as <code>search.m1.small</code>) on which an index partition is hosted.</p>"""
PartitionInstanceType: TypeAlias = Literal[
    "search.m1.small",
    "search.m1.large",
    "search.m2.xlarge",
    "search.m2.2xlarge",
    "search.m3.medium",
    "search.m3.large",
    "search.m3.xlarge",
    "search.m3.2xlarge",
    "search.small",
    "search.medium",
    "search.large",
    "search.xlarge",
    "search.2xlarge",
    "search.previousgeneration.small",
    "search.previousgeneration.large",
    "search.previousgeneration.xlarge",
    "search.previousgeneration.2xlarge",
]


# --- awsQuery ser/de ---
def to_query_text(value: PartitionInstanceType) -> str:
    return value


def from_query_text(text: str) -> PartitionInstanceType:
    return cast(PartitionInstanceType, text)


def serialize_query(
    value: PartitionInstanceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PartitionInstanceType:
    return from_query_text(el.text or "")
