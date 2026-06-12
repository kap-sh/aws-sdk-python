"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlCustomParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.security_control_custom_parameter

SecurityControlCustomParametersList: TypeAlias = list[
    "aws_sdk_securityhub.types.security_control_custom_parameter.SecurityControlCustomParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlCustomParametersList) -> list:
    import aws_sdk_securityhub.types.security_control_custom_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.security_control_custom_parameter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SecurityControlCustomParametersList:
    import aws_sdk_securityhub.types.security_control_custom_parameter

    out: SecurityControlCustomParametersList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.security_control_custom_parameter.deserialize_json(
                item
            )
        )
    return out
