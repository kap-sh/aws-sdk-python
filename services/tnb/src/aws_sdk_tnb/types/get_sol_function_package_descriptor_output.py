"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageDescriptorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.descriptor_content_type


class GetSolFunctionPackageDescriptorOutput(TypedDict, closed=True):
    content_type: NotRequired[
        "aws_sdk_tnb.types.descriptor_content_type.DescriptorContentType"
    ]
    """<p>Indicates the media type of the resource.</p>"""
    vnfd: NotRequired["bytes"]
    """<p>Contents of the function package descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageDescriptorOutput) -> dict:
    out: dict = {}
    if "vnfd" in value:
        import aws_sdk_tnb.types._prelude.blob

        out["vnfd"] = aws_sdk_tnb.types._prelude.blob.serialize_json(value["vnfd"])
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageDescriptorOutput:
    out: GetSolFunctionPackageDescriptorOutput = {}  # type: ignore[typeddict-item]
    if "vnfd" in data:
        import aws_sdk_tnb.types._prelude.blob

        out["vnfd"] = aws_sdk_tnb.types._prelude.blob.deserialize_json(data["vnfd"])
    return out
