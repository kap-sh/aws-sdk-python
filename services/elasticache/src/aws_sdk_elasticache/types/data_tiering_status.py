"""Generated from Smithy shape ``com.amazonaws.elasticache#DataTieringStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

DataTieringStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsQuery ser/de ---
def to_query_text(value: DataTieringStatus) -> str:
    return value


def from_query_text(text: str) -> DataTieringStatus:
    return cast(DataTieringStatus, text)


def serialize_query(
    value: DataTieringStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataTieringStatus:
    return from_query_text(el.text or "")
