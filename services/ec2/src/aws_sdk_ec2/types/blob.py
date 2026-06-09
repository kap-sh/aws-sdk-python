"""Generated from Smithy shape ``com.amazonaws.ec2#Blob``."""

import base64
from typing import TypeAlias

from aws_sdk_ec2._protocol.xml import Element

Blob: TypeAlias = bytes


# --- ec2Query ser/de ---
def to_ec2_query_text(value: Blob) -> str:
    return base64.b64encode(value).decode("ascii")


def from_ec2_query_text(text: str) -> Blob:
    return base64.b64decode(text)


def serialize_ec2_query(value: Blob, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> Blob:
    return from_ec2_query_text(el.text or "")
