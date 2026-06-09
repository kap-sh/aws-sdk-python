"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleConditionOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

IpamPrefixListResolverRuleConditionOperation: TypeAlias = Literal[
    "equals",
    "not-equals",
    "subnet-of",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "equals",
        "not-equals",
        "subnet-of",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "equals",
        "not-equals",
        "subnet-of",
    )
)


def to_ec2_query_text(value: IpamPrefixListResolverRuleConditionOperation) -> str:
    return value


def from_ec2_query_text(text: str) -> IpamPrefixListResolverRuleConditionOperation:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown IpamPrefixListResolverRuleConditionOperation value: {text!r}"
        )
    return cast(IpamPrefixListResolverRuleConditionOperation, text)


def serialize_ec2_query(
    value: IpamPrefixListResolverRuleConditionOperation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleConditionOperation:
    return from_ec2_query_text(el.text or "")
