"""Generated from Smithy shape ``com.amazonaws.route53#AccountLimitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53._protocol.xml import Element, SubElement

AccountLimitType: TypeAlias = Literal[
    "MAX_HEALTH_CHECKS_BY_OWNER",
    "MAX_HOSTED_ZONES_BY_OWNER",
    "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
    "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
    "MAX_TRAFFIC_POLICIES_BY_OWNER",
]


# --- restXml ser/de ---
def to_xml_text(value: AccountLimitType) -> str:
    return value


def from_xml_text(text: str) -> AccountLimitType:
    return cast(AccountLimitType, text)


def serialize_xml(value: AccountLimitType, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> AccountLimitType:
    return from_xml_text(el.text or "")
