"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginRestriction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.long_optional
    import aws_sdk_codeartifact.types.package_group_origin_restriction_mode
    import aws_sdk_codeartifact.types.package_group_reference


class PackageGroupOriginRestriction(TypedDict, closed=True):
    mode: NotRequired[
        "aws_sdk_codeartifact.types.package_group_origin_restriction_mode.PackageGroupOriginRestrictionMode"
    ]
    """<p>The package group origin restriction setting. If the value of <code>mode</code> is <code>ALLOW</code>, <code>ALLOW_SPECIFIC_REPOSITORIES</code>, or <code>BLOCK</code>, then the value of <code>effectiveMode</code> is the same. Otherwise, when the value is <code>INHERIT</code>, then the value of <code>effectiveMode</code> is the value of <code>mode</code> of the first parent group which does not have a value of <code>INHERIT</code>.</p>"""
    effective_mode: NotRequired[
        "aws_sdk_codeartifact.types.package_group_origin_restriction_mode.PackageGroupOriginRestrictionMode"
    ]
    """<p>The effective package group origin restriction setting. If the value of <code>mode</code> is <code>ALLOW</code>, <code>ALLOW_SPECIFIC_REPOSITORIES</code>, or <code>BLOCK</code>, then the value of <code>effectiveMode</code> is the same. Otherwise, when the value of <code>mode</code> is <code>INHERIT</code>, then the value of <code>effectiveMode</code> is the value of <code>mode</code> of the first parent group which does not have a value of <code>INHERIT</code>.</p>"""
    inherited_from: NotRequired[
        "aws_sdk_codeartifact.types.package_group_reference.PackageGroupReference"
    ]
    """<p>The parent package group that the package group origin restrictions are inherited from.</p>"""
    repositories_count: NotRequired[
        "aws_sdk_codeartifact.types.long_optional.LongOptional"
    ]
    """<p>The number of repositories in the allowed repository list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageGroupOriginRestriction) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_codeartifact.types.package_group_origin_restriction_mode

        out["mode"] = (
            aws_sdk_codeartifact.types.package_group_origin_restriction_mode.serialize_json(
                value["mode"]
            )
        )
    if "effective_mode" in value:
        import aws_sdk_codeartifact.types.package_group_origin_restriction_mode

        out["effectiveMode"] = (
            aws_sdk_codeartifact.types.package_group_origin_restriction_mode.serialize_json(
                value["effective_mode"]
            )
        )
    if "inherited_from" in value:
        import aws_sdk_codeartifact.types.package_group_reference

        out["inheritedFrom"] = (
            aws_sdk_codeartifact.types.package_group_reference.serialize_json(
                value["inherited_from"]
            )
        )
    if "repositories_count" in value:
        out["repositoriesCount"] = value["repositories_count"]
    return out


def deserialize_json(data: dict) -> PackageGroupOriginRestriction:
    out: PackageGroupOriginRestriction = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_codeartifact.types.package_group_origin_restriction_mode

        out["mode"] = (
            aws_sdk_codeartifact.types.package_group_origin_restriction_mode.deserialize_json(
                data["mode"]
            )
        )
    if "effectiveMode" in data:
        import aws_sdk_codeartifact.types.package_group_origin_restriction_mode

        out["effective_mode"] = (
            aws_sdk_codeartifact.types.package_group_origin_restriction_mode.deserialize_json(
                data["effectiveMode"]
            )
        )
    if "inheritedFrom" in data:
        import aws_sdk_codeartifact.types.package_group_reference

        out["inherited_from"] = (
            aws_sdk_codeartifact.types.package_group_reference.deserialize_json(
                data["inheritedFrom"]
            )
        )
    if "repositoriesCount" in data:
        out["repositories_count"] = data["repositoriesCount"]
    return out
