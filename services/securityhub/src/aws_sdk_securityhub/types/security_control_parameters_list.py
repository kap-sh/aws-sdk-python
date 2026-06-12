"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.security_control_parameter

SecurityControlParametersList: TypeAlias = list[
    "aws_sdk_securityhub.types.security_control_parameter.SecurityControlParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlParametersList) -> list:
    import aws_sdk_securityhub.types.security_control_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.security_control_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityControlParametersList:
    import aws_sdk_securityhub.types.security_control_parameter

    out: SecurityControlParametersList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.security_control_parameter.deserialize_json(item)
        )
    return out
