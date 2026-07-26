"""Generated from Smithy shape ``com.amazonaws.finspace#CustomDNSConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.custom_dns_server

CustomDNSConfiguration: TypeAlias = list[
    "capo_finspace.types.custom_dns_server.CustomDNSServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomDNSConfiguration) -> list:
    import capo_finspace.types.custom_dns_server

    out: list = []
    for item in value:
        out.append(capo_finspace.types.custom_dns_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomDNSConfiguration:
    import capo_finspace.types.custom_dns_server

    out: CustomDNSConfiguration = []
    for item in data:
        out.append(capo_finspace.types.custom_dns_server.deserialize_json(item))
    return out
