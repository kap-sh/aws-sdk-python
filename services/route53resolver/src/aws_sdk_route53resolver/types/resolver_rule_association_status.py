"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ResolverRuleAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "COMPLETE",
    "DELETING",
    "FAILED",
    "OVERRIDDEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "COMPLETE",
        "DELETING",
        "FAILED",
        "OVERRIDDEN",
    )
)


def serialize_aws_json_1_1(value: ResolverRuleAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverRuleAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResolverRuleAssociationStatus value: {data!r}"
        )
    return cast(ResolverRuleAssociationStatus, data)
