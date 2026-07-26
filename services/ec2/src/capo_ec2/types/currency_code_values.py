"""Generated from Smithy shape ``com.amazonaws.ec2#CurrencyCodeValues``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CurrencyCodeValues: TypeAlias = Literal["USD",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CurrencyCodeValues) -> str:
    return value


def from_ec2_query_text(text: str) -> CurrencyCodeValues:
    return cast(CurrencyCodeValues, text)


def serialize_ec2_query(
    value: CurrencyCodeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CurrencyCodeValues:
    return from_ec2_query_text(el.text or "")
