"""Generated from Smithy shape ``com.amazonaws.ec2#FindingsFound``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

FindingsFound: TypeAlias = Literal[
    "true",
    "false",
    "unknown",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FindingsFound) -> str:
    return value


def from_ec2_query_text(text: str) -> FindingsFound:
    return cast(FindingsFound, text)


def serialize_ec2_query(
    value: FindingsFound, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FindingsFound:
    return from_ec2_query_text(el.text or "")
