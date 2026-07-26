"""Generated from Smithy shape ``com.amazonaws.ec2#StatusName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

StatusName: TypeAlias = Literal["reachability",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: StatusName) -> str:
    return value


def from_ec2_query_text(text: str) -> StatusName:
    return cast(StatusName, text)


def serialize_ec2_query(
    value: StatusName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StatusName:
    return from_ec2_query_text(el.text or "")
