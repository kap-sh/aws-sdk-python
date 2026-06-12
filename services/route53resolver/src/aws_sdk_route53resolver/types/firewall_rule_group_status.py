"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallRuleGroupStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "DELETING",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: FirewallRuleGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallRuleGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallRuleGroupStatus value: {data!r}")
    return cast(FirewallRuleGroupStatus, data)
