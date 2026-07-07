"""Generated from Smithy shape ``com.amazonaws.qapps#PermissionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.action


class PermissionInput(TypedDict, closed=True):
    action: "aws_sdk_qapps.types.action.Action"
    """<p>The action associated with the permission.</p>"""
    principal: "str"
    """<p>The principal user to which the permission applies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionInput) -> dict:
    out: dict = {}
    import aws_sdk_qapps.types.action

    out["action"] = aws_sdk_qapps.types.action.serialize_json(value["action"])
    out["principal"] = value["principal"]
    return out


def deserialize_json(data: dict) -> PermissionInput:
    out: PermissionInput = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_qapps.types.action

        out["action"] = aws_sdk_qapps.types.action.deserialize_json(data["action"])
    else:
        raise DeserializationError("PermissionInput.action required")
    if "principal" in data:
        out["principal"] = data["principal"]
    else:
        raise DeserializationError("PermissionInput.principal required")
    return out
