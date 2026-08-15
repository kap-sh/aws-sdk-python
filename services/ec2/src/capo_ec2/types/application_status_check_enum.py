"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusCheckEnum``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ApplicationStatusCheckEnum: TypeAlias = Literal[
    "passed",
    "failed",
    "initializing",
    "insufficient-data",
    "not-applicable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ApplicationStatusCheckEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> ApplicationStatusCheckEnum:
    return cast(ApplicationStatusCheckEnum, text)


def serialize_ec2_query(
    value: ApplicationStatusCheckEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ApplicationStatusCheckEnum:
    return from_ec2_query_text(el.text or "")
