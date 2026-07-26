"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpdatePackageGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_description


class UpdatePackageGroupResult(TypedDict, closed=True):
    package_group: NotRequired[
        "capo_codeartifact.types.package_group_description.PackageGroupDescription"
    ]
    """<p> The package group and information about it after the request has been processed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageGroupResult) -> dict:
    out: dict = {}
    if "package_group" in value:
        import capo_codeartifact.types.package_group_description

        out["packageGroup"] = (
            capo_codeartifact.types.package_group_description.serialize_json(
                value["package_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageGroupResult:
    out: UpdatePackageGroupResult = {}  # type: ignore[typeddict-item]
    if "packageGroup" in data:
        import capo_codeartifact.types.package_group_description

        out["package_group"] = (
            capo_codeartifact.types.package_group_description.deserialize_json(
                data["packageGroup"]
            )
        )
    return out
