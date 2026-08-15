"""Generated from Smithy shape ``com.amazonaws.ec2#PayerResponsibilityScope``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

PayerResponsibilityScope: TypeAlias = Literal["vpc-endpoint-charges",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PayerResponsibilityScope) -> str:
    return value


def from_ec2_query_text(text: str) -> PayerResponsibilityScope:
    return cast(PayerResponsibilityScope, text)


def serialize_ec2_query(
    value: PayerResponsibilityScope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PayerResponsibilityScope:
    return from_ec2_query_text(el.text or "")
