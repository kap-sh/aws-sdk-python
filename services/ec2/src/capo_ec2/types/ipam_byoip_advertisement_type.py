"""Generated from Smithy shape ``com.amazonaws.ec2#IpamByoipAdvertisementType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The advertisement type of a BYOIP route.</p>"""
IpamByoipAdvertisementType: TypeAlias = Literal[
    "regional",
    "global",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamByoipAdvertisementType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamByoipAdvertisementType:
    return cast(IpamByoipAdvertisementType, text)


def serialize_ec2_query(
    value: IpamByoipAdvertisementType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamByoipAdvertisementType:
    return from_ec2_query_text(el.text or "")
