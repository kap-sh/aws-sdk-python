"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallRuleGroupAssociationStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: FirewallRuleGroupAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallRuleGroupAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FirewallRuleGroupAssociationStatus value: {data!r}"
        )
    return cast(FirewallRuleGroupAssociationStatus, data)
