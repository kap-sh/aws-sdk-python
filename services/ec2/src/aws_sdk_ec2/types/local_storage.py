"""Generated from Smithy shape ``com.amazonaws.ec2#LocalStorage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

LocalStorage: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: LocalStorage) -> str:
    return value


def from_ec2_query_text(text: str) -> LocalStorage:
    return cast(LocalStorage, text)


def serialize_ec2_query(
    value: LocalStorage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LocalStorage:
    return from_ec2_query_text(el.text or "")
