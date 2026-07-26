"""Generated from Smithy shape ``com.amazonaws.iam#BootstrapDatum``."""

import base64
from typing import TypeAlias

from capo_iam._protocol.xml import Element

BootstrapDatum: TypeAlias = bytes


# --- awsQuery ser/de ---
def to_query_text(value: BootstrapDatum) -> str:
    return base64.b64encode(value).decode("ascii")


def from_query_text(text: str) -> BootstrapDatum:
    return base64.b64decode(text)


def serialize_query(
    value: BootstrapDatum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BootstrapDatum:
    return from_query_text(el.text or "")
