"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolSourceResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamPoolSourceResourceType: TypeAlias = Literal["vpc",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("vpc",))


_VALUES: frozenset[str] = frozenset(("vpc",))


def to_ec2_query_text(value: IpamPoolSourceResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPoolSourceResourceType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown IpamPoolSourceResourceType value: {text!r}"
        )
    return cast(IpamPoolSourceResourceType, text)


def serialize_ec2_query(
    value: IpamPoolSourceResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPoolSourceResourceType:
    return from_ec2_query_text(el.text or "")
