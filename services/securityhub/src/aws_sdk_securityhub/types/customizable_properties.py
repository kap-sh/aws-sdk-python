"""Generated from Smithy shape ``com.amazonaws.securityhub#CustomizableProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.security_control_property

CustomizableProperties: TypeAlias = list[
    "aws_sdk_securityhub.types.security_control_property.SecurityControlProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomizableProperties) -> list:
    import aws_sdk_securityhub.types.security_control_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.security_control_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomizableProperties:
    import aws_sdk_securityhub.types.security_control_property

    out: CustomizableProperties = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.security_control_property.deserialize_json(item)
        )
    return out
