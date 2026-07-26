"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlCustomParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.security_control_custom_parameter

SecurityControlCustomParametersList: TypeAlias = list[
    "capo_securityhub.types.security_control_custom_parameter.SecurityControlCustomParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlCustomParametersList) -> list:
    import capo_securityhub.types.security_control_custom_parameter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.security_control_custom_parameter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SecurityControlCustomParametersList:
    import capo_securityhub.types.security_control_custom_parameter

    out: SecurityControlCustomParametersList = []
    for item in data:
        out.append(
            capo_securityhub.types.security_control_custom_parameter.deserialize_json(
                item
            )
        )
    return out
