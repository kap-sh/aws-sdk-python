"""Generated from Smithy shape ``com.amazonaws.appconfig#ExtensionAssociationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.identifier


class ExtensionAssociationSummary(TypedDict):
    id: NotRequired["aws_sdk_appconfig.types.identifier.Identifier"]
    """<p>The extension association ID. This ID is used to call other <code>ExtensionAssociation</code> API actions such as <code>GetExtensionAssociation</code> or <code>DeleteExtensionAssociation</code>.</p>"""
    extension_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The system-generated Amazon Resource Name (ARN) for the extension.</p>"""
    resource_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The ARNs of applications, configuration profiles, or environments defined in the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionAssociationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ExtensionAssociationSummary:
    out: ExtensionAssociationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ExtensionArn" in data:
        out["extension_arn"] = data["ExtensionArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
