"""Generated from Smithy shape ``com.amazonaws.wafv2#APIKeyTokenDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.token_domain

APIKeyTokenDomains: TypeAlias = list["capo_wafv2.types.token_domain.TokenDomain"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: APIKeyTokenDomains) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> APIKeyTokenDomains:
    return list(data)
