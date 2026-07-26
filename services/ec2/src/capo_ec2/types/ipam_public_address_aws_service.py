"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressAwsService``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

IpamPublicAddressAwsService: TypeAlias = Literal[
    "nat-gateway",
    "database-migration-service",
    "redshift",
    "elastic-container-service",
    "relational-database-service",
    "site-to-site-vpn",
    "load-balancer",
    "global-accelerator",
    "cloudfront",
    "other",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: IpamPublicAddressAwsService) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPublicAddressAwsService:
    return cast(IpamPublicAddressAwsService, text)


def serialize_ec2_query(
    value: IpamPublicAddressAwsService, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPublicAddressAwsService:
    return from_ec2_query_text(el.text or "")
