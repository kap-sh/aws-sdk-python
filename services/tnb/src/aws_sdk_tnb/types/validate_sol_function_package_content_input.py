"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolFunctionPackageContentInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.package_content_type
    import aws_sdk_tnb.types.sensitive_blob
    import aws_sdk_tnb.types.vnf_pkg_id


class ValidateSolFunctionPackageContentInput(TypedDict):
    vnf_pkg_id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    content_type: NotRequired[
        "aws_sdk_tnb.types.package_content_type.PackageContentType"
    ]
    """<p>Function package content type.</p>"""
    file: "aws_sdk_tnb.types.sensitive_blob.SensitiveBlob"
    """<p>Function package file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolFunctionPackageContentInput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.sensitive_blob

    out["file"] = aws_sdk_tnb.types.sensitive_blob.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> ValidateSolFunctionPackageContentInput:
    out: ValidateSolFunctionPackageContentInput = {}  # type: ignore[typeddict-item]
    if "file" in data:
        import aws_sdk_tnb.types.sensitive_blob

        out["file"] = aws_sdk_tnb.types.sensitive_blob.deserialize_json(data["file"])
    else:
        raise DeserializationError(
            "ValidateSolFunctionPackageContentInput.file required"
        )
    return out
