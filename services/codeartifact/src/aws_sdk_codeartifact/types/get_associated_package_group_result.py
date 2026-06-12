"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetAssociatedPackageGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_association_type
    import aws_sdk_codeartifact.types.package_group_description


class GetAssociatedPackageGroupResult(TypedDict):
    package_group: NotRequired[
        "aws_sdk_codeartifact.types.package_group_description.PackageGroupDescription"
    ]
    """<p>The package group that is associated with the requested package.</p>"""
    association_type: NotRequired[
        "aws_sdk_codeartifact.types.package_group_association_type.PackageGroupAssociationType"
    ]
    """<p>Describes the strength of the association between the package and package group. A strong match is also known as an exact match, and a weak match is known as a relative match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedPackageGroupResult) -> dict:
    out: dict = {}
    if "package_group" in value:
        import aws_sdk_codeartifact.types.package_group_description

        out["packageGroup"] = (
            aws_sdk_codeartifact.types.package_group_description.serialize_json(
                value["package_group"]
            )
        )
    if "association_type" in value:
        import aws_sdk_codeartifact.types.package_group_association_type

        out["associationType"] = (
            aws_sdk_codeartifact.types.package_group_association_type.serialize_json(
                value["association_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssociatedPackageGroupResult:
    out: GetAssociatedPackageGroupResult = {}  # type: ignore[typeddict-item]
    if "packageGroup" in data:
        import aws_sdk_codeartifact.types.package_group_description

        out["package_group"] = (
            aws_sdk_codeartifact.types.package_group_description.deserialize_json(
                data["packageGroup"]
            )
        )
    if "associationType" in data:
        import aws_sdk_codeartifact.types.package_group_association_type

        out["association_type"] = (
            aws_sdk_codeartifact.types.package_group_association_type.deserialize_json(
                data["associationType"]
            )
        )
    return out
