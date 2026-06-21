"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareStatusForProducer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

DataShareStatusForProducer: TypeAlias = Literal[
    "ACTIVE",
    "AUTHORIZED",
    "PENDING_AUTHORIZATION",
    "DEAUTHORIZED",
    "REJECTED",
]


# --- awsQuery ser/de ---
def to_query_text(value: DataShareStatusForProducer) -> str:
    return value


def from_query_text(text: str) -> DataShareStatusForProducer:
    return cast(DataShareStatusForProducer, text)


def serialize_query(
    value: DataShareStatusForProducer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataShareStatusForProducer:
    return from_query_text(el.text or "")
