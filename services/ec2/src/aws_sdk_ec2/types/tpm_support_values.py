"""Generated from Smithy shape ``com.amazonaws.ec2#TpmSupportValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TpmSupportValues: TypeAlias = Literal["v2.0",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TpmSupportValues) -> str:
    return value


def from_ec2_query_text(text: str) -> TpmSupportValues:
    return cast(TpmSupportValues, text)


def serialize_ec2_query(
    value: TpmSupportValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TpmSupportValues:
    return from_ec2_query_text(el.text or "")
