"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IdentityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.identity_provider_summary

IdentityProviderList: TypeAlias = list[
    "capo_workspaces_web.types.identity_provider_summary.IdentityProviderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderList) -> list:
    import capo_workspaces_web.types.identity_provider_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.identity_provider_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdentityProviderList:
    import capo_workspaces_web.types.identity_provider_summary

    out: IdentityProviderList = []
    for item in data:
        out.append(
            capo_workspaces_web.types.identity_provider_summary.deserialize_json(item)
        )
    return out
