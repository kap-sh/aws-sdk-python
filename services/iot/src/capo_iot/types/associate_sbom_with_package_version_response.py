"""Generated from Smithy shape ``com.amazonaws.iot#AssociateSbomWithPackageVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.package_name
    import capo_iot.types.sbom
    import capo_iot.types.sbom_validation_status
    import capo_iot.types.version_name


class AssociateSbomWithPackageVersionResponse(TypedDict, closed=True):
    package_name: NotRequired["capo_iot.types.package_name.PackageName"]
    """<p>The name of the new software package.</p>"""
    version_name: NotRequired["capo_iot.types.version_name.VersionName"]
    """<p>The name of the new package version.</p>"""
    sbom: NotRequired["capo_iot.types.sbom.Sbom"]
    sbom_validation_status: NotRequired[
        "capo_iot.types.sbom_validation_status.SbomValidationStatus"
    ]
    """<p>The status of the initial validation for the software bill of materials against the Software Package Data Exchange (SPDX) and CycloneDX industry standard formats.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSbomWithPackageVersionResponse) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "sbom" in value:
        import capo_iot.types.sbom

        out["sbom"] = capo_iot.types.sbom.serialize_json(value["sbom"])
    if "sbom_validation_status" in value:
        import capo_iot.types.sbom_validation_status

        out["sbomValidationStatus"] = (
            capo_iot.types.sbom_validation_status.serialize_json(
                value["sbom_validation_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateSbomWithPackageVersionResponse:
    out: AssociateSbomWithPackageVersionResponse = {}  # type: ignore[typeddict-item]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "sbom" in data:
        import capo_iot.types.sbom

        out["sbom"] = capo_iot.types.sbom.deserialize_json(data["sbom"])
    if "sbomValidationStatus" in data:
        import capo_iot.types.sbom_validation_status

        out["sbom_validation_status"] = (
            capo_iot.types.sbom_validation_status.deserialize_json(
                data["sbomValidationStatus"]
            )
        )
    return out
