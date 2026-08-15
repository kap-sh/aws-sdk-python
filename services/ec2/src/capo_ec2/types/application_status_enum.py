"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusEnum``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ApplicationStatusEnum: TypeAlias = Literal[
    "ok",
    "impaired",
    "initializing",
    "insufficient-data",
    "not-applicable",
    "suppressed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ApplicationStatusEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> ApplicationStatusEnum:
    return cast(ApplicationStatusEnum, text)


def serialize_ec2_query(
    value: ApplicationStatusEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ApplicationStatusEnum:
    return from_ec2_query_text(el.text or "")
