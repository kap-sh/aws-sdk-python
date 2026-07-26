"""Generated from Smithy shape ``com.amazonaws.appflow#CustomAuthConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.custom_auth_config

CustomAuthConfigList: TypeAlias = list[
    "capo_appflow.types.custom_auth_config.CustomAuthConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomAuthConfigList) -> list:
    import capo_appflow.types.custom_auth_config

    out: list = []
    for item in value:
        out.append(capo_appflow.types.custom_auth_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomAuthConfigList:
    import capo_appflow.types.custom_auth_config

    out: CustomAuthConfigList = []
    for item in data:
        out.append(capo_appflow.types.custom_auth_config.deserialize_json(item))
    return out
