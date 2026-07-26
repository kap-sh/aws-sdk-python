"""Generated from Smithy shape ``com.amazonaws.iam#assertionEncryptionModeType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

assertionEncryptionModeType: TypeAlias = Literal[
    "Required",
    "Allowed",
]


# --- awsQuery ser/de ---
def to_query_text(value: assertionEncryptionModeType) -> str:
    return value


def from_query_text(text: str) -> assertionEncryptionModeType:
    return cast(assertionEncryptionModeType, text)


def serialize_query(
    value: assertionEncryptionModeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> assertionEncryptionModeType:
    return from_query_text(el.text or "")
