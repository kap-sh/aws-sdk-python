"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionInvocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.identifier
    import aws_sdk_appconfig.types.name
    import aws_sdk_appconfig.types.string
    import aws_sdk_appconfig.types.uri


class ActionInvocation(TypedDict):
    extension_identifier: NotRequired["aws_sdk_appconfig.types.identifier.Identifier"]
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    action_name: NotRequired["aws_sdk_appconfig.types.name.Name"]
    """<p>The name of the action.</p>"""
    uri: NotRequired["aws_sdk_appconfig.types.uri.Uri"]
    """<p>The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.</p>"""
    role_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>An Amazon Resource Name (ARN) for an Identity and Access Management assume role.</p>"""
    error_message: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>The error message when an extension invocation fails.</p>"""
    error_code: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>The error code when an extension invocation fails.</p>"""
    invocation_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>A system-generated ID for this invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionInvocation) -> dict:
    out: dict = {}
    if "extension_identifier" in value:
        out["ExtensionIdentifier"] = value["extension_identifier"]
    if "action_name" in value:
        out["ActionName"] = value["action_name"]
    if "uri" in value:
        out["Uri"] = value["uri"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "invocation_id" in value:
        out["InvocationId"] = value["invocation_id"]
    return out


def deserialize_json(data: dict) -> ActionInvocation:
    out: ActionInvocation = {}  # type: ignore[typeddict-item]
    if "ExtensionIdentifier" in data:
        out["extension_identifier"] = data["ExtensionIdentifier"]
    if "ActionName" in data:
        out["action_name"] = data["ActionName"]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "InvocationId" in data:
        out["invocation_id"] = data["InvocationId"]
    return out
