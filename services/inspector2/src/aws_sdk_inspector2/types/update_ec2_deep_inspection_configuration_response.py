"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateEc2DeepInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ec2_deep_inspection_status
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.path_list


class UpdateEc2DeepInspectionConfigurationResponse(TypedDict):
    package_paths: NotRequired["aws_sdk_inspector2.types.path_list.PathList"]
    """<p>The current Amazon Inspector deep inspection custom paths for your account.</p>"""
    org_package_paths: NotRequired["aws_sdk_inspector2.types.path_list.PathList"]
    """<p>The current Amazon Inspector deep inspection custom paths for the organization.</p>"""
    status: NotRequired[
        "aws_sdk_inspector2.types.ec2_deep_inspection_status.Ec2DeepInspectionStatus"
    ]
    """<p>The status of Amazon Inspector deep inspection in your account.</p>"""
    error_message: NotRequired[
        "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """<p>An error message explaining why new Amazon Inspector deep inspection custom paths could not be added.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEc2DeepInspectionConfigurationResponse) -> dict:
    out: dict = {}
    if "package_paths" in value:
        import aws_sdk_inspector2.types.path_list

        out["packagePaths"] = aws_sdk_inspector2.types.path_list.serialize_json(
            value["package_paths"]
        )
    if "org_package_paths" in value:
        import aws_sdk_inspector2.types.path_list

        out["orgPackagePaths"] = aws_sdk_inspector2.types.path_list.serialize_json(
            value["org_package_paths"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> UpdateEc2DeepInspectionConfigurationResponse:
    out: UpdateEc2DeepInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "packagePaths" in data:
        import aws_sdk_inspector2.types.path_list

        out["package_paths"] = aws_sdk_inspector2.types.path_list.deserialize_json(
            data["packagePaths"]
        )
    if "orgPackagePaths" in data:
        import aws_sdk_inspector2.types.path_list

        out["org_package_paths"] = aws_sdk_inspector2.types.path_list.deserialize_json(
            data["orgPackagePaths"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
