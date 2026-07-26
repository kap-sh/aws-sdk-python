"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScopeExternalAuthorityType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamScopeExternalAuthorityType: TypeAlias = Literal["infoblox",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamScopeExternalAuthorityType) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamScopeExternalAuthorityType:
    return cast(IpamScopeExternalAuthorityType, text)


def serialize_ec2_query(
    value: IpamScopeExternalAuthorityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamScopeExternalAuthorityType:
    return from_ec2_query_text(el.text or "")
