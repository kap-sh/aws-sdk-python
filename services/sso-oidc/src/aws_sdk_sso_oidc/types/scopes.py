"""Generated from Smithy shape ``com.amazonaws.ssooidc#Scopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.scope

Scopes: TypeAlias = list["aws_sdk_sso_oidc.types.scope.Scope"]


# --- restJson1 ser/de ---
def serialize_json(value: Scopes) -> list:
    return list(value)


def deserialize_json(data: list) -> Scopes:
    return list(data)
