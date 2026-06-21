"""Generated from Smithy shape ``com.amazonaws.ec2#SummaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

SummaryStatus: TypeAlias = Literal[
    "ok",
    "impaired",
    "insufficient-data",
    "not-applicable",
    "initializing",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SummaryStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> SummaryStatus:
    return cast(SummaryStatus, text)


def serialize_ec2_query(
    value: SummaryStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SummaryStatus:
    return from_ec2_query_text(el.text or "")
