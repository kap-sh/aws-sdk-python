"""Generated from Smithy shape ``com.amazonaws.iot#DeletePackageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.client_token
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.version_name


class DeletePackageVersionRequest(TypedDict, closed=True):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the associated software package.</p>"""
    version_name: "aws_sdk_iot.types.version_name.VersionName"
    """<p>The name of the target package version.</p>"""
    client_token: NotRequired["aws_sdk_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackageVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackageVersionRequest:
    out: DeletePackageVersionRequest = {}  # type: ignore[typeddict-item]
    return out
