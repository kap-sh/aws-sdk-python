"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainRedirectionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallDomainRedirectionAction: TypeAlias = Literal[
    "INSPECT_REDIRECTION_DOMAIN",
    "TRUST_REDIRECTION_DOMAIN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSPECT_REDIRECTION_DOMAIN",
        "TRUST_REDIRECTION_DOMAIN",
    )
)


def serialize_aws_json_1_1(value: FirewallDomainRedirectionAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainRedirectionAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FirewallDomainRedirectionAction value: {data!r}"
        )
    return cast(FirewallDomainRedirectionAction, data)
