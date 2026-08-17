"""Generated from Smithy shape ``com.amazonaws.ssooidc#RedirectUris``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_oidc.types.uri

RedirectUris: TypeAlias = list["capo_sso_oidc.types.uri.URI"]


# --- restJson1 ser/de ---
def serialize_json(value: RedirectUris) -> list:
    return list(value)


def deserialize_json(data: list) -> RedirectUris:
    return [item for item in data if item is not None]
