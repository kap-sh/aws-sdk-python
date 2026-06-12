"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeletePackageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_summary


class DeletePackageResult(TypedDict):
    deleted_package: NotRequired[
        "aws_sdk_codeartifact.types.package_summary.PackageSummary"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageResult) -> dict:
    out: dict = {}
    if "deleted_package" in value:
        import aws_sdk_codeartifact.types.package_summary

        out["deletedPackage"] = (
            aws_sdk_codeartifact.types.package_summary.serialize_json(
                value["deleted_package"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeletePackageResult:
    out: DeletePackageResult = {}  # type: ignore[typeddict-item]
    if "deletedPackage" in data:
        import aws_sdk_codeartifact.types.package_summary

        out["deleted_package"] = (
            aws_sdk_codeartifact.types.package_summary.deserialize_json(
                data["deletedPackage"]
            )
        )
    return out
