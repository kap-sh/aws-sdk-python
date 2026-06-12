"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_control

StandardsControls: TypeAlias = list[
    "aws_sdk_securityhub.types.standards_control.StandardsControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControls) -> list:
    import aws_sdk_securityhub.types.standards_control

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.standards_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> StandardsControls:
    import aws_sdk_securityhub.types.standards_control

    out: StandardsControls = []
    for item in data:
        out.append(aws_sdk_securityhub.types.standards_control.deserialize_json(item))
    return out
