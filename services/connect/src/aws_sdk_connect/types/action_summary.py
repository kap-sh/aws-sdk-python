"""Generated from Smithy shape ``com.amazonaws.connect#ActionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.action_type


class ActionSummary(TypedDict):
    action_type: "aws_sdk_connect.types.action_type.ActionType"
    """<p>The action type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummary) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.action_type

    out["ActionType"] = aws_sdk_connect.types.action_type.serialize_json(
        value["action_type"]
    )
    return out


def deserialize_json(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        import aws_sdk_connect.types.action_type

        out["action_type"] = aws_sdk_connect.types.action_type.deserialize_json(
            data["ActionType"]
        )
    else:
        raise DeserializationError("ActionSummary.action_type required")
    return out
