"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.creation_date
    import aws_sdk_iot.types.last_modified_date
    import aws_sdk_iot.types.package_arn
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.resource_description
    import aws_sdk_iot.types.version_name


class GetPackageResponse(TypedDict, closed=True):
    package_name: NotRequired["aws_sdk_iot.types.package_name.PackageName"]
    """<p>The name of the software package.</p>"""
    package_arn: NotRequired["aws_sdk_iot.types.package_arn.PackageArn"]
    """<p>The ARN for the package.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.resource_description.ResourceDescription"
    ]
    """<p>The package description.</p>"""
    default_version_name: NotRequired["aws_sdk_iot.types.version_name.VersionName"]
    """<p>The name of the default package version.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The date the package was created.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date when the package was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageResponse) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
    if "package_arn" in value:
        out["packageArn"] = value["package_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "default_version_name" in value:
        out["defaultVersionName"] = value["default_version_name"]
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
    return out


def deserialize_json(data: dict) -> GetPackageResponse:
    out: GetPackageResponse = {}  # type: ignore[typeddict-item]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
    if "packageArn" in data:
        out["package_arn"] = data["packageArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "defaultVersionName" in data:
        out["default_version_name"] = data["defaultVersionName"]
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
    return out
