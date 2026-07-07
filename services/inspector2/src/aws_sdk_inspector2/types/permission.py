"""Generated from Smithy shape ``com.amazonaws.inspector2#Permission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.operation
    import aws_sdk_inspector2.types.service


class Permission(TypedDict, closed=True):
    service: "aws_sdk_inspector2.types.service.Service"
    """<p>The services that the permissions allow an account to perform the given operations for.</p>"""
    operation: "aws_sdk_inspector2.types.operation.Operation"
    """<p>The operations that can be performed with the given permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> dict:
    out: dict = {}
    out["service"] = value["service"]
    out["operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("Permission.service required")
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError("Permission.operation required")
    return out
