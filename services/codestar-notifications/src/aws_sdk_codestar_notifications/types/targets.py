"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#Targets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codestar_notifications.types.target

Targets: TypeAlias = list["aws_sdk_codestar_notifications.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: Targets) -> list:
    import aws_sdk_codestar_notifications.types.target

    out: list = []
    for item in value:
        out.append(aws_sdk_codestar_notifications.types.target.serialize_json(item))
    return out


def deserialize_json(data: list) -> Targets:
    import aws_sdk_codestar_notifications.types.target

    out: Targets = []
    for item in data:
        out.append(aws_sdk_codestar_notifications.types.target.deserialize_json(item))
    return out
