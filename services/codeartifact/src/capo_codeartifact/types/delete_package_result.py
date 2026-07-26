"""Generated from Smithy shape ``com.amazonaws.codeartifact#DeletePackageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_summary


class DeletePackageResult(TypedDict, closed=True):
    deleted_package: NotRequired[
        "capo_codeartifact.types.package_summary.PackageSummary"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageResult) -> dict:
    out: dict = {}
    if "deleted_package" in value:
        import capo_codeartifact.types.package_summary

        out["deletedPackage"] = capo_codeartifact.types.package_summary.serialize_json(
            value["deleted_package"]
        )
    return out


def deserialize_json(data: dict) -> DeletePackageResult:
    out: DeletePackageResult = {}  # type: ignore[typeddict-item]
    if "deletedPackage" in data:
        import capo_codeartifact.types.package_summary

        out["deleted_package"] = (
            capo_codeartifact.types.package_summary.deserialize_json(
                data["deletedPackage"]
            )
        )
    return out
