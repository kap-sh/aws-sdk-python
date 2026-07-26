"""Generated from Smithy shape ``com.amazonaws.ec2#ActivityStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ActivityStatus: TypeAlias = Literal[
    "error",
    "pending_fulfillment",
    "pending_termination",
    "fulfilled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ActivityStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ActivityStatus:
    return cast(ActivityStatus, text)


def serialize_ec2_query(
    value: ActivityStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ActivityStatus:
    return from_ec2_query_text(el.text or "")
