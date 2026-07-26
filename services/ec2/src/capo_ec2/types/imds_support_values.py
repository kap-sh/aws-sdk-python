"""Generated from Smithy shape ``com.amazonaws.ec2#ImdsSupportValues``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ImdsSupportValues: TypeAlias = Literal["v2.0",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ImdsSupportValues) -> str:
    return value


def from_ec2_query_text(text: str) -> ImdsSupportValues:
    return cast(ImdsSupportValues, text)


def serialize_ec2_query(
    value: ImdsSupportValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImdsSupportValues:
    return from_ec2_query_text(el.text or "")
