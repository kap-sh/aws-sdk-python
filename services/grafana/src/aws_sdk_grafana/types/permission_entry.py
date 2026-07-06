"""Generated from Smithy shape ``com.amazonaws.grafana#PermissionEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.role
    import aws_sdk_grafana.types.user


class PermissionEntry(TypedDict, closed=True):
    user: "aws_sdk_grafana.types.user.User"
    """<p>A structure with the ID of the user or group with this role.</p>"""
    role: "aws_sdk_grafana.types.role.Role"
    """<p>Specifies whether the user or group has the <code>Admin</code>, <code>Editor</code>, or <code>Viewer</code> role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionEntry) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.user

    out["user"] = aws_sdk_grafana.types.user.serialize_json(value["user"])
    out["role"] = value["role"]
    return out


def deserialize_json(data: dict) -> PermissionEntry:
    out: PermissionEntry = {}  # type: ignore[typeddict-item]
    if "user" in data:
        import aws_sdk_grafana.types.user

        out["user"] = aws_sdk_grafana.types.user.deserialize_json(data["user"])
    else:
        raise DeserializationError("PermissionEntry.user required")
    if "role" in data:
        out["role"] = data["role"]
    else:
        raise DeserializationError("PermissionEntry.role required")
    return out
