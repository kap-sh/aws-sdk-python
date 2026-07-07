"""Generated from Smithy shape ``com.amazonaws.eks#LaunchTemplateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class LaunchTemplateSpecification(TypedDict, closed=True):
    name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template name or the launch template ID in the request, but not both. After node group creation, you cannot use a different name.</p>"""
    version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The version number of the launch template to use. If no version is specified, then the template's default version is used. You can use a different version for node group updates.</p>"""
    id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name in the request, but not both. After node group creation, you cannot use a different ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateSpecification) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> LaunchTemplateSpecification:
    out: LaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "id" in data:
        out["id"] = data["id"]
    return out
