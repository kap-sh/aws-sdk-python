"""Generated from Smithy shape ``com.amazonaws.iot#AssociateSbomWithPackageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.client_token
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.sbom
    import aws_sdk_iot.types.version_name


class AssociateSbomWithPackageVersionRequest(TypedDict, closed=True):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the new software package.</p>"""
    version_name: "aws_sdk_iot.types.version_name.VersionName"
    """<p>The name of the new package version.</p>"""
    sbom: "aws_sdk_iot.types.sbom.Sbom"
    client_token: NotRequired["aws_sdk_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSbomWithPackageVersionRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.sbom

    out["sbom"] = aws_sdk_iot.types.sbom.serialize_json(value["sbom"])
    return out


def deserialize_json(data: dict) -> AssociateSbomWithPackageVersionRequest:
    out: AssociateSbomWithPackageVersionRequest = {}  # type: ignore[typeddict-item]
    if "sbom" in data:
        import aws_sdk_iot.types.sbom

        out["sbom"] = aws_sdk_iot.types.sbom.deserialize_json(data["sbom"])
    else:
        raise DeserializationError(
            "AssociateSbomWithPackageVersionRequest.sbom required"
        )
    return out
