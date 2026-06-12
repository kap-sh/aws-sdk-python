"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainUpdateOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallDomainUpdateOperation: TypeAlias = Literal[
    "ADD",
    "REMOVE",
    "REPLACE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "REMOVE",
        "REPLACE",
    )
)


def serialize_aws_json_1_1(value: FirewallDomainUpdateOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainUpdateOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FirewallDomainUpdateOperation value: {data!r}"
        )
    return cast(FirewallDomainUpdateOperation, data)
