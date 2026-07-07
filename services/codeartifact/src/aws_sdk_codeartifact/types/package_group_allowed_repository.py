"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAllowedRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_origin_restriction_type
    import aws_sdk_codeartifact.types.repository_name


class PackageGroupAllowedRepository(TypedDict, closed=True):
    repository_name: NotRequired[
        "aws_sdk_codeartifact.types.repository_name.RepositoryName"
    ]
    """<p> The name of the allowed repository. </p>"""
    origin_restriction_type: NotRequired[
        "aws_sdk_codeartifact.types.package_group_origin_restriction_type.PackageGroupOriginRestrictionType"
    ]
    """<p>The origin configuration restriction type of the allowed repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupAllowedRepository) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "origin_restriction_type" in value:
        import aws_sdk_codeartifact.types.package_group_origin_restriction_type

        out["originRestrictionType"] = (
            aws_sdk_codeartifact.types.package_group_origin_restriction_type.serialize_json(
                value["origin_restriction_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageGroupAllowedRepository:
    out: PackageGroupAllowedRepository = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "originRestrictionType" in data:
        import aws_sdk_codeartifact.types.package_group_origin_restriction_type

        out["origin_restriction_type"] = (
            aws_sdk_codeartifact.types.package_group_origin_restriction_type.deserialize_json(
                data["originRestrictionType"]
            )
        )
    return out
