"""Generated from Smithy shape ``com.amazonaws.ec2#RecurringChargeFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RecurringChargeFrequency: TypeAlias = Literal["Hourly",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RecurringChargeFrequency) -> str:
    return value


def from_ec2_query_text(text: str) -> RecurringChargeFrequency:
    return cast(RecurringChargeFrequency, text)


def serialize_ec2_query(
    value: RecurringChargeFrequency, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RecurringChargeFrequency:
    return from_ec2_query_text(el.text or "")
