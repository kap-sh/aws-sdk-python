"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageGroupOriginConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.origin_restrictions
    import aws_sdk_codeartifact.types.package_group_allowed_repository_list
    import aws_sdk_codeartifact.types.package_group_pattern


class UpdatePackageGroupOriginConfigurationRequest(TypedDict):
    domain: "aws_sdk_codeartifact.types.domain_name.DomainName"
    """<p> The name of the domain which contains the package group for which to update the origin configuration. </p>"""
    domain_owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    package_group: (
        "aws_sdk_codeartifact.types.package_group_pattern.PackageGroupPattern"
    )
    """<p> The pattern of the package group for which to update the origin configuration. </p>"""
    restrictions: NotRequired[
        "aws_sdk_codeartifact.types.origin_restrictions.OriginRestrictions"
    ]
    """<p> The origin configuration settings that determine how package versions can enter repositories. </p>"""
    add_allowed_repositories: NotRequired[
        "aws_sdk_codeartifact.types.package_group_allowed_repository_list.PackageGroupAllowedRepositoryList"
    ]
    """<p>The repository name and restrictions to add to the allowed repository list of the specified package group.</p>"""
    remove_allowed_repositories: NotRequired[
        "aws_sdk_codeartifact.types.package_group_allowed_repository_list.PackageGroupAllowedRepositoryList"
    ]
    """<p>The repository name and restrictions to remove from the allowed repository list of the specified package group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageGroupOriginConfigurationRequest) -> dict:
    out: dict = {}
    if "restrictions" in value:
        import aws_sdk_codeartifact.types.origin_restrictions

        out["restrictions"] = (
            aws_sdk_codeartifact.types.origin_restrictions.serialize_json(
                value["restrictions"]
            )
        )
    if "add_allowed_repositories" in value:
        import aws_sdk_codeartifact.types.package_group_allowed_repository_list

        out["addAllowedRepositories"] = (
            aws_sdk_codeartifact.types.package_group_allowed_repository_list.serialize_json(
                value["add_allowed_repositories"]
            )
        )
    if "remove_allowed_repositories" in value:
        import aws_sdk_codeartifact.types.package_group_allowed_repository_list

        out["removeAllowedRepositories"] = (
            aws_sdk_codeartifact.types.package_group_allowed_repository_list.serialize_json(
                value["remove_allowed_repositories"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageGroupOriginConfigurationRequest:
    out: UpdatePackageGroupOriginConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "restrictions" in data:
        import aws_sdk_codeartifact.types.origin_restrictions

        out["restrictions"] = (
            aws_sdk_codeartifact.types.origin_restrictions.deserialize_json(
                data["restrictions"]
            )
        )
    if "addAllowedRepositories" in data:
        import aws_sdk_codeartifact.types.package_group_allowed_repository_list

        out["add_allowed_repositories"] = (
            aws_sdk_codeartifact.types.package_group_allowed_repository_list.deserialize_json(
                data["addAllowedRepositories"]
            )
        )
    if "removeAllowedRepositories" in data:
        import aws_sdk_codeartifact.types.package_group_allowed_repository_list

        out["remove_allowed_repositories"] = (
            aws_sdk_codeartifact.types.package_group_allowed_repository_list.deserialize_json(
                data["removeAllowedRepositories"]
            )
        )
    return out
