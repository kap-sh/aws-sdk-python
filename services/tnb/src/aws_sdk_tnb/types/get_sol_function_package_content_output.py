"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.package_content_type


class GetSolFunctionPackageContentOutput(TypedDict, closed=True):
    content_type: NotRequired[
        "aws_sdk_tnb.types.package_content_type.PackageContentType"
    ]
    """<p>Indicates the media type of the resource.</p>"""
    package_content: NotRequired["bytes"]
    """<p>Contents of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageContentOutput) -> dict:
    out: dict = {}
    if "package_content" in value:
        import aws_sdk_tnb.types._prelude.blob

        out["packageContent"] = aws_sdk_tnb.types._prelude.blob.serialize_json(
            value["package_content"]
        )
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageContentOutput:
    out: GetSolFunctionPackageContentOutput = {}  # type: ignore[typeddict-item]
    if "packageContent" in data:
        import aws_sdk_tnb.types._prelude.blob

        out["package_content"] = aws_sdk_tnb.types._prelude.blob.deserialize_json(
            data["packageContent"]
        )
    return out
