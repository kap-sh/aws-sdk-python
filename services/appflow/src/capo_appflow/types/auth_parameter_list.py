"""Generated from Smithy shape ``com.amazonaws.appflow#AuthParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.auth_parameter

AuthParameterList: TypeAlias = list["capo_appflow.types.auth_parameter.AuthParameter"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthParameterList) -> list:
    import capo_appflow.types.auth_parameter

    out: list = []
    for item in value:
        out.append(capo_appflow.types.auth_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthParameterList:
    import capo_appflow.types.auth_parameter

    out: AuthParameterList = []
    for item in data:
        out.append(capo_appflow.types.auth_parameter.deserialize_json(item))
    return out
