"""Generated from Smithy shape ``com.amazonaws.quicksight#DnsResolverList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.i_pv4_address

DnsResolverList: TypeAlias = list["capo_quicksight.types.i_pv4_address.IPv4Address"]


# --- restJson1 ser/de ---
def serialize_json(value: DnsResolverList) -> list:
    return list(value)


def deserialize_json(data: list) -> DnsResolverList:
    return list(data)
