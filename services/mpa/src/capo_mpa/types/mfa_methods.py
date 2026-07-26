"""Generated from Smithy shape ``com.amazonaws.mpa#MfaMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.mfa_method

MfaMethods: TypeAlias = list["capo_mpa.types.mfa_method.MfaMethod"]


# --- restJson1 ser/de ---
def serialize_json(value: MfaMethods) -> list:
    import capo_mpa.types.mfa_method

    out: list = []
    for item in value:
        out.append(capo_mpa.types.mfa_method.serialize_json(item))
    return out


def deserialize_json(data: list) -> MfaMethods:
    import capo_mpa.types.mfa_method

    out: MfaMethods = []
    for item in data:
        out.append(capo_mpa.types.mfa_method.deserialize_json(item))
    return out
