"""Generated from Smithy shape ``com.amazonaws.iot#AuthResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.auth_result

AuthResults: TypeAlias = list["aws_sdk_iot.types.auth_result.AuthResult"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthResults) -> list:
    import aws_sdk_iot.types.auth_result

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.auth_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthResults:
    import aws_sdk_iot.types.auth_result

    out: AuthResults = []
    for item in data:
        out.append(aws_sdk_iot.types.auth_result.deserialize_json(item))
    return out
