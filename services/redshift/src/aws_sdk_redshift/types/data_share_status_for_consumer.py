"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareStatusForConsumer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

DataShareStatusForConsumer: TypeAlias = Literal[
    "ACTIVE",
    "AVAILABLE",
]


# --- awsQuery ser/de ---
def to_query_text(value: DataShareStatusForConsumer) -> str:
    return value


def from_query_text(text: str) -> DataShareStatusForConsumer:
    return cast(DataShareStatusForConsumer, text)


def serialize_query(
    value: DataShareStatusForConsumer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataShareStatusForConsumer:
    return from_query_text(el.text or "")
