"""Generated from Smithy shape ``com.amazonaws.backup#FrameworkControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.framework_control

FrameworkControls: TypeAlias = list[
    "aws_sdk_backup.types.framework_control.FrameworkControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkControls) -> list:
    import aws_sdk_backup.types.framework_control

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.framework_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> FrameworkControls:
    import aws_sdk_backup.types.framework_control

    out: FrameworkControls = []
    for item in data:
        out.append(aws_sdk_backup.types.framework_control.deserialize_json(item))
    return out
