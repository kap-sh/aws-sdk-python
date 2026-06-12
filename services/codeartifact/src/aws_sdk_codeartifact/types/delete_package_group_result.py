"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeletePackageGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_group_description


class DeletePackageGroupResult(TypedDict):
    package_group: NotRequired[
        "aws_sdk_codeartifact.types.package_group_description.PackageGroupDescription"
    ]
    """<p> Information about the deleted package group after processing the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageGroupResult) -> dict:
    out: dict = {}
    if "package_group" in value:
        import aws_sdk_codeartifact.types.package_group_description

        out["packageGroup"] = (
            aws_sdk_codeartifact.types.package_group_description.serialize_json(
                value["package_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeletePackageGroupResult:
    out: DeletePackageGroupResult = {}  # type: ignore[typeddict-item]
    if "packageGroup" in data:
        import aws_sdk_codeartifact.types.package_group_description

        out["package_group"] = (
            aws_sdk_codeartifact.types.package_group_description.deserialize_json(
                data["packageGroup"]
            )
        )
    return out
