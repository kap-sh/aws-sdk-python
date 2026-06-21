"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedNetworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

AssociatedNetworkType: TypeAlias = Literal["vpc",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AssociatedNetworkType) -> str:
    return value


def from_ec2_query_text(text: str) -> AssociatedNetworkType:
    return cast(AssociatedNetworkType, text)


def serialize_ec2_query(
    value: AssociatedNetworkType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AssociatedNetworkType:
    return from_ec2_query_text(el.text or "")
