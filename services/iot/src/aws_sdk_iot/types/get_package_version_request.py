"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.version_name


class GetPackageVersionRequest(TypedDict):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the associated package.</p>"""
    version_name: "aws_sdk_iot.types.version_name.VersionName"
    """<p>The name of the target package version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPackageVersionRequest:
    out: GetPackageVersionRequest = {}  # type: ignore[typeddict-item]
    return out
