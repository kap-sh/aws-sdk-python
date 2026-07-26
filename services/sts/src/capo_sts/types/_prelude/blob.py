"""Generated from Smithy prelude shape ``smithy.api#Blob``."""

import base64

from capo_sts._protocol.xml import Element


# --- awsQuery ser/de ---
def to_query_text(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def from_query_text(text: str) -> bytes:
    return base64.b64decode(text)


def serialize_query(value: bytes, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> bytes:
    return from_query_text(el.text or "")
