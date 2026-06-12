"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_module_description
    import aws_sdk_connect.types.resource_version


class ContactFlowModuleVersionSummary(TypedDict):
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module version.</p>"""
    version_description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module version.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleVersionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ContactFlowModuleVersionSummary:
    out: ContactFlowModuleVersionSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
