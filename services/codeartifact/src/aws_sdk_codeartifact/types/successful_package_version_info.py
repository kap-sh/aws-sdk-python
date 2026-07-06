"""Generated from Smithy shape ``com.amazonaws.codeartifact#SuccessfulPackageVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_version_status
    import aws_sdk_codeartifact.types.string


class SuccessfulPackageVersionInfo(TypedDict, closed=True):
    revision: NotRequired["aws_sdk_codeartifact.types.string.String"]
    """<p> The revision of a package version. </p>"""
    status: NotRequired[
        "aws_sdk_codeartifact.types.package_version_status.PackageVersionStatus"
    ]
    """<p> The status of a package version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulPackageVersionInfo) -> dict:
    out: dict = {}
    if "revision" in value:
        out["revision"] = value["revision"]
    if "status" in value:
        import aws_sdk_codeartifact.types.package_version_status

        out["status"] = (
            aws_sdk_codeartifact.types.package_version_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuccessfulPackageVersionInfo:
    out: SuccessfulPackageVersionInfo = {}  # type: ignore[typeddict-item]
    if "revision" in data:
        out["revision"] = data["revision"]
    if "status" in data:
        import aws_sdk_codeartifact.types.package_version_status

        out["status"] = (
            aws_sdk_codeartifact.types.package_version_status.deserialize_json(
                data["status"]
            )
        )
    return out
