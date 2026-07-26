"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DnsTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.dns_token

DnsTokenList: TypeAlias = list["capo_pinpoint_email.types.dns_token.DnsToken"]


# --- restJson1 ser/de ---
def serialize_json(value: DnsTokenList) -> list:
    return list(value)


def deserialize_json(data: list) -> DnsTokenList:
    return list(data)
