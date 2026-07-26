"""Generated from Smithy shape ``com.amazonaws.iot#AuthInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.auth_info

AuthInfos: TypeAlias = list["capo_iot.types.auth_info.AuthInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthInfos) -> list:
    import capo_iot.types.auth_info

    out: list = []
    for item in value:
        out.append(capo_iot.types.auth_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthInfos:
    import capo_iot.types.auth_info

    out: AuthInfos = []
    for item in data:
        out.append(capo_iot.types.auth_info.deserialize_json(item))
    return out
