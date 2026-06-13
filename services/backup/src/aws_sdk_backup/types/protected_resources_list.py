"""Generated from Smithy shape ``com.amazonaws.backup#ProtectedResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.protected_resource

ProtectedResourcesList: TypeAlias = list[
    "aws_sdk_backup.types.protected_resource.ProtectedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedResourcesList) -> list:
    import aws_sdk_backup.types.protected_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.protected_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtectedResourcesList:
    import aws_sdk_backup.types.protected_resource

    out: ProtectedResourcesList = []
    for item in data:
        out.append(aws_sdk_backup.types.protected_resource.deserialize_json(item))
    return out
