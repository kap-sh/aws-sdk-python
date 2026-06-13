"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string


class ActionSummary(TypedDict):
    action_identifier: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The identifier of an Amazon Q Business plugin action.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The display name assigned by Amazon Q Business to a plugin action. You can't modify this value.</p>"""
    instruction_example: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>An Amazon Q Business suggested prompt and end user can use to invoke a plugin action. This value can be modified and sent as input to initiate an action. For example:</p> <ul> <li> <p>Create a Jira task</p> </li> <li> <p>Create a chat assistant task to find the root cause of a specific incident</p> </li> </ul>"""
    description: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The description of an Amazon Q Business plugin action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummary) -> dict:
    out: dict = {}
    if "action_identifier" in value:
        out["actionIdentifier"] = value["action_identifier"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "instruction_example" in value:
        out["instructionExample"] = value["instruction_example"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if "actionIdentifier" in data:
        out["action_identifier"] = data["actionIdentifier"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "instructionExample" in data:
        out["instruction_example"] = data["instructionExample"]
    if "description" in data:
        out["description"] = data["description"]
    return out
