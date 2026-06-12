"""Generated from Smithy shape ``com.amazonaws.sns#Binary``."""

import base64
from typing import TypeAlias

from aws_sdk_sns._protocol.xml import Element

Binary: TypeAlias = bytes


# --- awsQuery ser/de ---
def to_query_text(value: Binary) -> str:
    return base64.b64encode(value).decode("ascii")


def from_query_text(text: str) -> Binary:
    return base64.b64decode(text)


def serialize_query(value: Binary, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Binary:
    return from_query_text(el.text or "")
