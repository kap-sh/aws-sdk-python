"""Generated from Smithy shape ``com.amazonaws.ec2#InitializationType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

InitializationType: TypeAlias = Literal[
    "default",
    "provisioned-rate",
    "volume-copy",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: InitializationType) -> str:
    return value


def from_ec2_query_text(text: str) -> InitializationType:
    return cast(InitializationType, text)


def serialize_ec2_query(
    value: InitializationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InitializationType:
    return from_ec2_query_text(el.text or "")
