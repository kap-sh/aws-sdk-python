"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRpkiStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The RPKI validation status of a BGP route.</p>"""
IpamRpkiStatus: TypeAlias = Literal[
    "valid",
    "invalid",
    "unknown",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamRpkiStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamRpkiStatus:
    return cast(IpamRpkiStatus, text)


def serialize_ec2_query(
    value: IpamRpkiStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamRpkiStatus:
    return from_ec2_query_text(el.text or "")
