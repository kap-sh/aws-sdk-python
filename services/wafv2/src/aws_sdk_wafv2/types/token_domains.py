"""Generated from Smithy shape ``com.amazonaws.wafv2#TokenDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.token_domain

TokenDomains: TypeAlias = list["aws_sdk_wafv2.types.token_domain.TokenDomain"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TokenDomains) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TokenDomains:
    return list(data)
