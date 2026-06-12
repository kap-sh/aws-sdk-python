"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverRuleStatus: TypeAlias = Literal[
    "COMPLETE",
    "DELETING",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "DELETING",
        "UPDATING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ResolverRuleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolverRuleStatus value: {data!r}")
    return cast(ResolverRuleStatus, data)
