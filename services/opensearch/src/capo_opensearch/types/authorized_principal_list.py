"""Generated from Smithy shape ``com.amazonaws.opensearch#AuthorizedPrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.authorized_principal

AuthorizedPrincipalList: TypeAlias = list[
    "capo_opensearch.types.authorized_principal.AuthorizedPrincipal"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedPrincipalList) -> list:
    import capo_opensearch.types.authorized_principal

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.authorized_principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthorizedPrincipalList:
    import capo_opensearch.types.authorized_principal

    out: AuthorizedPrincipalList = []
    for item in data:
        out.append(capo_opensearch.types.authorized_principal.deserialize_json(item))
    return out
