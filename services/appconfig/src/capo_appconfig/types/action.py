"""Generated from Smithy shape ``com.amazonaws.appconfig#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.description
    import capo_appconfig.types.name
    import capo_appconfig.types.uri


class Action(TypedDict, closed=True):
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The action name.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Information about the action.</p>"""
    uri: NotRequired["capo_appconfig.types.uri.Uri"]
    """<p>The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.</p>"""
    role_arn: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>An Amazon Resource Name (ARN) for an Identity and Access Management assume role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "uri" in value:
        out["Uri"] = value["uri"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
