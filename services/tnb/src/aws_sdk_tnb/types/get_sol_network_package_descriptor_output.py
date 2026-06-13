"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageDescriptorOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.descriptor_content_type


class GetSolNetworkPackageDescriptorOutput(TypedDict):
    content_type: NotRequired[
        "aws_sdk_tnb.types.descriptor_content_type.DescriptorContentType"
    ]
    """<p>Indicates the media type of the resource.</p>"""
    nsd: NotRequired["bytes"]
    """<p>Contents of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageDescriptorOutput) -> dict:
    out: dict = {}
    if "nsd" in value:
        import aws_sdk_tnb.types._prelude.blob

        out["nsd"] = aws_sdk_tnb.types._prelude.blob.serialize_json(value["nsd"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageDescriptorOutput:
    out: GetSolNetworkPackageDescriptorOutput = {}  # type: ignore[typeddict-item]
    if "nsd" in data:
        import aws_sdk_tnb.types._prelude.blob

        out["nsd"] = aws_sdk_tnb.types._prelude.blob.deserialize_json(data["nsd"])
    return out
