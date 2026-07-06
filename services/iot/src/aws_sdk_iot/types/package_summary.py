"""Generated from Smithy shape ``com.amazonaws.iot#PackageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.creation_date
    import aws_sdk_iot.types.last_modified_date
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.version_name


class PackageSummary(TypedDict, closed=True):
    package_name: NotRequired["aws_sdk_iot.types.package_name.PackageName"]
    """<p>The name for the target software package.</p>"""
    default_version_name: NotRequired["aws_sdk_iot.types.version_name.VersionName"]
    """<p>The name of the default package version.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.creation_date.CreationDate"]
    """<p>The date that the package was created.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_iot.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date that the package was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageSummary) -> dict:
    out: dict = {}
    if "package_name" in value:
        out["packageName"] = value["package_name"]
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


def deserialize_json(data: dict) -> PackageSummary:
    out: PackageSummary = {}  # type: ignore[typeddict-item]
    if "packageName" in data:
        out["package_name"] = data["packageName"]
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
