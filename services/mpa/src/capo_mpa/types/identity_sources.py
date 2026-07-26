"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.identity_source_for_list

IdentitySources: TypeAlias = list[
    "capo_mpa.types.identity_source_for_list.IdentitySourceForList"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySources) -> list:
    import capo_mpa.types.identity_source_for_list

    out: list = []
    for item in value:
        out.append(capo_mpa.types.identity_source_for_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdentitySources:
    import capo_mpa.types.identity_source_for_list

    out: IdentitySources = []
    for item in data:
        out.append(capo_mpa.types.identity_source_for_list.deserialize_json(item))
    return out
