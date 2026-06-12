"""Generated from Smithy shape ``com.amazonaws.grafana#PermissionEntryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_grafana.types.permission_entry

PermissionEntryList: TypeAlias = list["aws_sdk_grafana.types.permission_entry.PermissionEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionEntryList) -> list:
    import aws_sdk_grafana.types.permission_entry
    out: list = []
    for item in value:
        out.append(aws_sdk_grafana.types.permission_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionEntryList:
    import aws_sdk_grafana.types.permission_entry
    out: PermissionEntryList = []
    for item in data:
        out.append(aws_sdk_grafana.types.permission_entry.deserialize_json(item))
    return out