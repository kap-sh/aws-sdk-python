"""Generated from Smithy shape ``com.amazonaws.ssooidc#GrantTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_oidc.types.grant_type

GrantTypes: TypeAlias = list["aws_sdk_sso_oidc.types.grant_type.GrantType"]


# --- restJson1 ser/de ---
def serialize_json(value: GrantTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> GrantTypes:
    return list(data)
