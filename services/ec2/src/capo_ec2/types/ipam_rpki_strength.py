"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRpkiStrength``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The RPKI enforcement strength for route protection.</p>"""
IpamRpkiStrength: TypeAlias = Literal[
    "strict",
    "permissive",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamRpkiStrength) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamRpkiStrength:
    return cast(IpamRpkiStrength, text)


def serialize_ec2_query(
    value: IpamRpkiStrength, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamRpkiStrength:
    return from_ec2_query_text(el.text or "")
