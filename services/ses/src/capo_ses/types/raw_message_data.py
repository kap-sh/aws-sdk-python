"""Generated from Smithy shape ``com.amazonaws.ses#RawMessageData``."""

import base64
from typing import TypeAlias

from capo_ses._protocol.xml import Element

RawMessageData: TypeAlias = bytes


# --- awsQuery ser/de ---
def to_query_text(value: RawMessageData) -> str:
    return base64.b64encode(value).decode("ascii")


def from_query_text(text: str) -> RawMessageData:
    return base64.b64decode(text)


def serialize_query(
    value: RawMessageData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RawMessageData:
    return from_query_text(el.text or "")
