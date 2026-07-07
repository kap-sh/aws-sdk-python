"""Generated from Smithy shape ``com.amazonaws.tnb#ValidateSolNetworkPackageContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.package_content_type
    import aws_sdk_tnb.types.sensitive_blob


class ValidateSolNetworkPackageContentInput(TypedDict, closed=True):
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network service descriptor file.</p>"""
    content_type: NotRequired[
        "aws_sdk_tnb.types.package_content_type.PackageContentType"
    ]
    """<p>Network package content type.</p>"""
    file: "aws_sdk_tnb.types.sensitive_blob.SensitiveBlob"
    """<p>Network package file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSolNetworkPackageContentInput) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types.sensitive_blob

    out["file"] = aws_sdk_tnb.types.sensitive_blob.serialize_json(value["file"])
    return out


def deserialize_json(data: dict) -> ValidateSolNetworkPackageContentInput:
    out: ValidateSolNetworkPackageContentInput = {}  # type: ignore[typeddict-item]
    if "file" in data:
        import aws_sdk_tnb.types.sensitive_blob

        out["file"] = aws_sdk_tnb.types.sensitive_blob.deserialize_json(data["file"])
    else:
        raise DeserializationError(
            "ValidateSolNetworkPackageContentInput.file required"
        )
    return out
