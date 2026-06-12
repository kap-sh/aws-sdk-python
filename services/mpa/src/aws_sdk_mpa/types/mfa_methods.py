"""Generated from Smithy shape ``com.amazonaws.mpa#MfaMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.mfa_method

MfaMethods: TypeAlias = list["aws_sdk_mpa.types.mfa_method.MfaMethod"]


# --- restJson1 ser/de ---
def serialize_json(value: MfaMethods) -> list:
    import aws_sdk_mpa.types.mfa_method

    out: list = []
    for item in value:
        out.append(aws_sdk_mpa.types.mfa_method.serialize_json(item))
    return out


def deserialize_json(data: list) -> MfaMethods:
    import aws_sdk_mpa.types.mfa_method

    out: MfaMethods = []
    for item in data:
        out.append(aws_sdk_mpa.types.mfa_method.deserialize_json(item))
    return out
