"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IdentityProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.string_type

IdentityProviderDetails: TypeAlias = dict[
    "capo_workspaces_web.types.string_type.StringType",
    "capo_workspaces_web.types.string_type.StringType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: IdentityProviderDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> IdentityProviderDetails:
    out: IdentityProviderDetails = {}
    for key, value in data.items():
        out[key] = value
    return out
