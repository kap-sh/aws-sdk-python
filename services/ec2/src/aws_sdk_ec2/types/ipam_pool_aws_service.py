"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAwsService``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamPoolAwsService: TypeAlias = Literal[
    "ec2",
    "global-services",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ec2",
        "global-services",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ec2",
        "global-services",
    )
)


def to_ec2_query_text(value: IpamPoolAwsService) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPoolAwsService:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IpamPoolAwsService value: {text!r}")
    return cast(IpamPoolAwsService, text)


def serialize_ec2_query(
    value: IpamPoolAwsService, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPoolAwsService:
    return from_ec2_query_text(el.text or "")
