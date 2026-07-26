"""Generated from Smithy shape ``com.amazonaws.elasticache#DestinationType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

DestinationType: TypeAlias = Literal[
    "cloudwatch-logs",
    "kinesis-firehose",
]


# --- awsQuery ser/de ---
def to_query_text(value: DestinationType) -> str:
    return value


def from_query_text(text: str) -> DestinationType:
    return cast(DestinationType, text)


def serialize_query(
    value: DestinationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DestinationType:
    return from_query_text(el.text or "")
