"""Generated from Smithy shape ``com.amazonaws.route53domains#ListDomainsAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

ListDomainsAttributeName: TypeAlias = Literal[
    "DomainName",
    "Expiry",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DomainName",
        "Expiry",
    )
)


def serialize_aws_json_1_1(value: ListDomainsAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListDomainsAttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListDomainsAttributeName value: {data!r}")
    return cast(ListDomainsAttributeName, data)
