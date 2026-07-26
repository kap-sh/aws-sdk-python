"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfOAuthScopesElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifybackend.types.o_auth_scopes_element

ListOfOAuthScopesElement: TypeAlias = list[
    "capo_amplifybackend.types.o_auth_scopes_element.OAuthScopesElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfOAuthScopesElement) -> list:
    import capo_amplifybackend.types.o_auth_scopes_element

    out: list = []
    for item in value:
        out.append(capo_amplifybackend.types.o_auth_scopes_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfOAuthScopesElement:
    import capo_amplifybackend.types.o_auth_scopes_element

    out: ListOfOAuthScopesElement = []
    for item in data:
        out.append(
            capo_amplifybackend.types.o_auth_scopes_element.deserialize_json(item)
        )
    return out
