"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2CustomPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.o_auth2_custom_parameter

OAuth2CustomPropertiesList: TypeAlias = list[
    "capo_appflow.types.o_auth2_custom_parameter.OAuth2CustomParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2CustomPropertiesList) -> list:
    import capo_appflow.types.o_auth2_custom_parameter

    out: list = []
    for item in value:
        out.append(capo_appflow.types.o_auth2_custom_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OAuth2CustomPropertiesList:
    import capo_appflow.types.o_auth2_custom_parameter

    out: OAuth2CustomPropertiesList = []
    for item in data:
        out.append(capo_appflow.types.o_auth2_custom_parameter.deserialize_json(item))
    return out
