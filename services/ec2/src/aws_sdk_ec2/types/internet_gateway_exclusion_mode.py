"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayExclusionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

InternetGatewayExclusionMode: TypeAlias = Literal[
    "allow-bidirectional",
    "allow-egress",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "allow-bidirectional",
        "allow-egress",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "allow-bidirectional",
        "allow-egress",
    )
)


def to_ec2_query_text(value: InternetGatewayExclusionMode) -> str:
    return value


def from_ec2_query_text(text: str) -> InternetGatewayExclusionMode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown InternetGatewayExclusionMode value: {text!r}"
        )
    return cast(InternetGatewayExclusionMode, text)


def serialize_ec2_query(
    value: InternetGatewayExclusionMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> InternetGatewayExclusionMode:
    return from_ec2_query_text(el.text or "")
