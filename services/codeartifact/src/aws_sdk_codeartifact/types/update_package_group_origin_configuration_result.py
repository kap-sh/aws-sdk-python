"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageGroupOriginConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_allowed_repository_updates
    import aws_sdk_codeartifact.types.package_group_description


class UpdatePackageGroupOriginConfigurationResult(TypedDict):
    package_group: NotRequired[
        "aws_sdk_codeartifact.types.package_group_description.PackageGroupDescription"
    ]
    """<p> The package group and information about it after processing the request. </p>"""
    allowed_repository_updates: NotRequired[
        "aws_sdk_codeartifact.types.package_group_allowed_repository_updates.PackageGroupAllowedRepositoryUpdates"
    ]
    """<p>Information about the updated allowed repositories after processing the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageGroupOriginConfigurationResult) -> dict:
    out: dict = {}
    if "package_group" in value:
        import aws_sdk_codeartifact.types.package_group_description

        out["packageGroup"] = (
            aws_sdk_codeartifact.types.package_group_description.serialize_json(
                value["package_group"]
            )
        )
    if "allowed_repository_updates" in value:
        import aws_sdk_codeartifact.types.package_group_allowed_repository_updates

        out["allowedRepositoryUpdates"] = (
            aws_sdk_codeartifact.types.package_group_allowed_repository_updates.serialize_json(
                value["allowed_repository_updates"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageGroupOriginConfigurationResult:
    out: UpdatePackageGroupOriginConfigurationResult = {}  # type: ignore[typeddict-item]
    if "packageGroup" in data:
        import aws_sdk_codeartifact.types.package_group_description

        out["package_group"] = (
            aws_sdk_codeartifact.types.package_group_description.deserialize_json(
                data["packageGroup"]
            )
        )
    if "allowedRepositoryUpdates" in data:
        import aws_sdk_codeartifact.types.package_group_allowed_repository_updates

        out["allowed_repository_updates"] = (
            aws_sdk_codeartifact.types.package_group_allowed_repository_updates.deserialize_json(
                data["allowedRepositoryUpdates"]
            )
        )
    return out
