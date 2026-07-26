"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.access_type

AccessTypeList: TypeAlias = list["capo_securitylake.types.access_type.AccessType"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessTypeList) -> list:
    import capo_securitylake.types.access_type

    out: list = []
    for item in value:
        out.append(capo_securitylake.types.access_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessTypeList:
    import capo_securitylake.types.access_type

    out: AccessTypeList = []
    for item in data:
        out.append(capo_securitylake.types.access_type.deserialize_json(item))
    return out
