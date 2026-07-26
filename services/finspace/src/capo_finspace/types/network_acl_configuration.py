"""Generated from Smithy shape ``com.amazonaws.finspace#NetworkACLConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.network_acl_entry

NetworkACLConfiguration: TypeAlias = list[
    "capo_finspace.types.network_acl_entry.NetworkACLEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkACLConfiguration) -> list:
    import capo_finspace.types.network_acl_entry

    out: list = []
    for item in value:
        out.append(capo_finspace.types.network_acl_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkACLConfiguration:
    import capo_finspace.types.network_acl_entry

    out: NetworkACLConfiguration = []
    for item in data:
        out.append(capo_finspace.types.network_acl_entry.deserialize_json(item))
    return out
