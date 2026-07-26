"""Generated from Smithy shape ``com.amazonaws.elasticache#StorageEncryptionType``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

StorageEncryptionType: TypeAlias = Literal[
    "none",
    "sse-elasticache",
    "sse-kms",
]


# --- awsQuery ser/de ---
def to_query_text(value: StorageEncryptionType) -> str:
    return value


def from_query_text(text: str) -> StorageEncryptionType:
    return cast(StorageEncryptionType, text)


def serialize_query(
    value: StorageEncryptionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StorageEncryptionType:
    return from_query_text(el.text or "")
