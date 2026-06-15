"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateEc2DeepInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.path_list


class UpdateEc2DeepInspectionConfigurationRequest(TypedDict):
    activate_deep_inspection: NotRequired["bool"]
    r"""<p>Specify <code>TRUE</code> to activate Amazon Inspector deep inspection in your account, or <code>FALSE</code> to deactivate. Member accounts in an organization cannot deactivate deep inspection, instead the delegated administrator for the organization can deactivate a member account using <a href=\"https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html\">BatchUpdateMemberEc2DeepInspectionStatus</a>.</p>"""
    package_paths: NotRequired["aws_sdk_inspector2.types.path_list.PathList"]
    """<p>The Amazon Inspector deep inspection custom paths you are adding for your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEc2DeepInspectionConfigurationRequest) -> dict:
    out: dict = {}
    if "activate_deep_inspection" in value:
        out["activateDeepInspection"] = value["activate_deep_inspection"]
    if "package_paths" in value:
        import aws_sdk_inspector2.types.path_list

        out["packagePaths"] = aws_sdk_inspector2.types.path_list.serialize_json(
            value["package_paths"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEc2DeepInspectionConfigurationRequest:
    out: UpdateEc2DeepInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "activateDeepInspection" in data:
        out["activate_deep_inspection"] = data["activateDeepInspection"]
    if "packagePaths" in data:
        import aws_sdk_inspector2.types.path_list

        out["package_paths"] = aws_sdk_inspector2.types.path_list.deserialize_json(
            data["packagePaths"]
        )
    return out
