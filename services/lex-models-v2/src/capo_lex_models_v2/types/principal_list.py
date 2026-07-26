"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.principal

PrincipalList: TypeAlias = list["capo_lex_models_v2.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalList) -> list:
    import capo_lex_models_v2.types.principal

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrincipalList:
    import capo_lex_models_v2.types.principal

    out: PrincipalList = []
    for item in data:
        out.append(capo_lex_models_v2.types.principal.deserialize_json(item))
    return out
