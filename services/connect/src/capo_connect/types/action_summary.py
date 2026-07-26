"""Generated from Smithy shape ``com.amazonaws.connect#ActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.action_type


class ActionSummary(TypedDict, closed=True):
    action_type: "capo_connect.types.action_type.ActionType"
    """<p>The action type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummary) -> dict:
    out: dict = {}
    import capo_connect.types.action_type

    out["ActionType"] = capo_connect.types.action_type.serialize_json(
        value["action_type"]
    )
    return out


def deserialize_json(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if "ActionType" in data:
        import capo_connect.types.action_type

        out["action_type"] = capo_connect.types.action_type.deserialize_json(
            data["ActionType"]
        )
    else:
        raise DeserializationError("ActionSummary.action_type required")
    return out
