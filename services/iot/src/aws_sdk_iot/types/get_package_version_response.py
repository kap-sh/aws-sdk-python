"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.creation_date
    import aws_sdk_iot.types.last_modified_date
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.package_version_arn
    import aws_sdk_iot.types.package_version_artifact
    import aws_sdk_iot.types.package_version_error_reason
    import aws_sdk_iot.types.package_version_recipe
    import aws_sdk_iot.types.package_version_status
    import aws_sdk_iot.types.resource_attributes
    import aws_sdk_iot.types.resource_description
    import aws_sdk_iot.types.sbom
    import aws_sdk_iot.types.sbom_validation_status
    import aws_sdk_iot.types.version_name


class GetPackageVersionResponse(TypedDict):
    package_version_arn: NotRequired[
        "aws_sdk_iot.types.package_version_arn.PackageVersionArn"
    ]
    """<p>The ARN for the package version.</p>"""
    package_name: NotRequired["aws_sdk_iot.types.package_name.PackageName"]
    """<p>The name of the software package.</p>"""
    version_name: NotRequired["aws_sdk_iot.types.version_name.VersionName"]
    """<p>The name of the package version.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.resource_description.ResourceDescription"
    ]
    """<p>The package version description.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.resource_attributes.ResourceAttributes"]
    """<p>Metadata that were added to the package version that can be used to define a package version’s configuration.</p>"""
    artifact: NotRequired[
        "aws_sdk_iot.types.package_version_artifact.PackageVersionArtifact"
    ]
    """<p>The various components that make up a software package version.</p>"""
    status: NotRequired["aws_sdk_iot.types.package_version_status.PackageVersionStatus"]
    """<p>The status associated to the package version. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle\">Package version lifecycle</a>.</p>"""
    error_reason: NotRequired[
        "aws_sdk_iot.types.package_version_error_reason.PackageVersionErrorReason"
    ]
    """<p>Error reason for a package version failure during creation or update.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The date when the package version was created.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the package version was last updated.</p>"""
    sbom: NotRequired["aws_sdk_iot.types.sbom.Sbom"]
    """<p>The software bill of materials for a software package version.</p>"""
    sbom_validation_status: NotRequired[
        "aws_sdk_iot.types.sbom_validation_status.SbomValidationStatus"
    ]
    """<p>The status of the validation for a new software bill of materials added to a software package version.</p>"""
    recipe: NotRequired["aws_sdk_iot.types.package_version_recipe.PackageVersionRecipe"]
    """<p>The inline job document associated with a software package version used for a quick job deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionResponse) -> dict:
    out: dict = {}
    if "package_version_arn" in value:
        out["packageVersionArn"] = value["package_version_arn"]
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "attributes" in value:
        import aws_sdk_iot.types.resource_attributes

        out["attributes"] = aws_sdk_iot.types.resource_attributes.serialize_json(
            value["attributes"]
        )
    if "artifact" in value:
        import aws_sdk_iot.types.package_version_artifact

        out["artifact"] = aws_sdk_iot.types.package_version_artifact.serialize_json(
            value["artifact"]
        )
    if "status" in value:
        import aws_sdk_iot.types.package_version_status

        out["status"] = aws_sdk_iot.types.package_version_status.serialize_json(
            value["status"]
        )
    if "error_reason" in value:
        out["errorReason"] = value["error_reason"]
    if "creation_date" in value:
        import aws_sdk_iot.types.creation_date

        out["creationDate"] = aws_sdk_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.last_modified_date

        out["lastModifiedDate"] = aws_sdk_iot.types.last_modified_date.serialize_json(
            value["last_modified_date"]
        )
    if "sbom" in value:
        import aws_sdk_iot.types.sbom

        out["sbom"] = aws_sdk_iot.types.sbom.serialize_json(value["sbom"])
    if "sbom_validation_status" in value:
        import aws_sdk_iot.types.sbom_validation_status

        out["sbomValidationStatus"] = (
            aws_sdk_iot.types.sbom_validation_status.serialize_json(
                value["sbom_validation_status"]
            )
        )
    if "recipe" in value:
        out["recipe"] = value["recipe"]
    return out


def deserialize_json(data: dict) -> GetPackageVersionResponse:
    out: GetPackageVersionResponse = {}  # type: ignore[typeddict-item]
    if "packageVersionArn" in data:
        out["package_version_arn"] = data["packageVersionArn"]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    if "description" in data:
        out["description"] = data["description"]
    if "attributes" in data:
        import aws_sdk_iot.types.resource_attributes

        out["attributes"] = aws_sdk_iot.types.resource_attributes.deserialize_json(
            data["attributes"]
        )
    if "artifact" in data:
        import aws_sdk_iot.types.package_version_artifact

        out["artifact"] = aws_sdk_iot.types.package_version_artifact.deserialize_json(
            data["artifact"]
        )
    if "status" in data:
        import aws_sdk_iot.types.package_version_status

        out["status"] = aws_sdk_iot.types.package_version_status.deserialize_json(
            data["status"]
        )
    if "errorReason" in data:
        out["error_reason"] = data["errorReason"]
    if "creationDate" in data:
        import aws_sdk_iot.types.creation_date

        out["creation_date"] = aws_sdk_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_iot.types.last_modified_date.deserialize_json(
                data["lastModifiedDate"]
            )
        )
    if "sbom" in data:
        import aws_sdk_iot.types.sbom

        out["sbom"] = aws_sdk_iot.types.sbom.deserialize_json(data["sbom"])
    if "sbomValidationStatus" in data:
        import aws_sdk_iot.types.sbom_validation_status

        out["sbom_validation_status"] = (
            aws_sdk_iot.types.sbom_validation_status.deserialize_json(
                data["sbomValidationStatus"]
            )
        )
    if "recipe" in data:
        out["recipe"] = data["recipe"]
    return out
