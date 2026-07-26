"""Generated from Smithy shape ``com.amazonaws.ec2#KeyType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

KeyType: TypeAlias = Literal[
    "rsa",
    "ed25519",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: KeyType) -> str:
    return value


def from_ec2_query_text(text: str) -> KeyType:
    return cast(KeyType, text)


def serialize_ec2_query(
    value: KeyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> KeyType:
    return from_ec2_query_text(el.text or "")
