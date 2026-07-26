"""Generated from Smithy shape ``com.amazonaws.iot#AuthResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.auth_result

AuthResults: TypeAlias = list["capo_iot.types.auth_result.AuthResult"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthResults) -> list:
    import capo_iot.types.auth_result

    out: list = []
    for item in value:
        out.append(capo_iot.types.auth_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthResults:
    import capo_iot.types.auth_result

    out: AuthResults = []
    for item in data:
        out.append(capo_iot.types.auth_result.deserialize_json(item))
    return out
