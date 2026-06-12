"""Generated from Smithy shape ``com.amazonaws.ssooidc#RedirectUris``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.uri

RedirectUris: TypeAlias = list["aws_sdk_sso_oidc.types.uri.URI"]


# --- restJson1 ser/de ---
def serialize_json(value: RedirectUris) -> list:
    return list(value)


def deserialize_json(data: list) -> RedirectUris:
    return list(data)
