"""Generated from Smithy shape ``com.amazonaws.connect#SecurityKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.security_key

SecurityKeysList: TypeAlias = list["capo_connect.types.security_key.SecurityKey"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityKeysList) -> list:
    import capo_connect.types.security_key

    out: list = []
    for item in value:
        out.append(capo_connect.types.security_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecurityKeysList:
    import capo_connect.types.security_key

    out: SecurityKeysList = []
    for item in data:
        out.append(capo_connect.types.security_key.deserialize_json(item))
    return out
