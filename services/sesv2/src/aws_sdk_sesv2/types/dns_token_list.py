"""Generated from Smithy shape ``com.amazonaws.sesv2#DnsTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.dns_token

DnsTokenList: TypeAlias = list["aws_sdk_sesv2.types.dns_token.DnsToken"]


# --- restJson1 ser/de ---
def serialize_json(value: DnsTokenList) -> list:
    return list(value)


def deserialize_json(data: list) -> DnsTokenList:
    return list(data)
