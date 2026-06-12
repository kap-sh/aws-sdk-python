"""Generated from Smithy shape ``com.amazonaws.appflow#OAuthScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.o_auth_scope

OAuthScopeList: TypeAlias = list["aws_sdk_appflow.types.o_auth_scope.OAuthScope"]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthScopeList) -> list:
    return list(value)


def deserialize_json(data: list) -> OAuthScopeList:
    return list(data)
