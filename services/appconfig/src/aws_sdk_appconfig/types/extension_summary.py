"""Generated from Smithy shape ``com.amazonaws.appconfig#ExtensionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.name


class ExtensionSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The system-generated ID of the extension.</p>"""
    name: NotRequired["aws_sdk_appconfig.types.name.Name"]
    """<p>The extension name.</p>"""
    version_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The extension version number.</p>"""
    arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The system-generated Amazon Resource Name (ARN) for the extension.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>Information about the extension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    out["VersionNumber"] = value.get("version_number", 0)
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ExtensionSummary:
    out: ExtensionSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    else:
        out["version_number"] = 0
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
