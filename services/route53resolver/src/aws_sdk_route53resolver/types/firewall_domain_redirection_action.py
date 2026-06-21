"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallDomainRedirectionAction``."""

from typing import Literal, TypeAlias, cast

FirewallDomainRedirectionAction: TypeAlias = Literal[
    "INSPECT_REDIRECTION_DOMAIN",
    "TRUST_REDIRECTION_DOMAIN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallDomainRedirectionAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDomainRedirectionAction:
    return cast(FirewallDomainRedirectionAction, data)
