"""Generated from Smithy shape ``com.amazonaws.iot#AuthInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.action_type
    import aws_sdk_iot.types.resources


class AuthInfo(TypedDict):
    action_type: NotRequired["aws_sdk_iot.types.action_type.ActionType"]
    """<p>The type of action for which the principal is being authorized.</p>"""
    resources: "aws_sdk_iot.types.resources.Resources"
    """<p>The resources for which the principal is being authorized to perform the specified action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthInfo) -> dict:
    out: dict = {}
    if "action_type" in value:
        import aws_sdk_iot.types.action_type

        out["actionType"] = aws_sdk_iot.types.action_type.serialize_json(
            value["action_type"]
        )
    import aws_sdk_iot.types.resources

    out["resources"] = aws_sdk_iot.types.resources.serialize_json(value["resources"])
    return out


def deserialize_json(data: dict) -> AuthInfo:
    out: AuthInfo = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        import aws_sdk_iot.types.action_type

        out["action_type"] = aws_sdk_iot.types.action_type.deserialize_json(
            data["actionType"]
        )
    if "resources" in data:
        import aws_sdk_iot.types.resources

        out["resources"] = aws_sdk_iot.types.resources.deserialize_json(
            data["resources"]
        )
    else:
        raise DeserializationError("AuthInfo.resources required")
    return out
