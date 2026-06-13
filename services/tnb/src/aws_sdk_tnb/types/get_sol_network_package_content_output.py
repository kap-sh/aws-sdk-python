"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageContentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.package_content_type


class GetSolNetworkPackageContentOutput(TypedDict):
    content_type: NotRequired[
        "aws_sdk_tnb.types.package_content_type.PackageContentType"
    ]
    """<p>Indicates the media type of the resource.</p>"""
    nsd_content: NotRequired["bytes"]
    """<p>Content of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageContentOutput) -> dict:
    out: dict = {}
    if "nsd_content" in value:
        import aws_sdk_tnb.types._prelude.blob

        out["nsdContent"] = aws_sdk_tnb.types._prelude.blob.serialize_json(
            value["nsd_content"]
        )
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageContentOutput:
    out: GetSolNetworkPackageContentOutput = {}  # type: ignore[typeddict-item]
    if "nsdContent" in data:
        import aws_sdk_tnb.types._prelude.blob

        out["nsd_content"] = aws_sdk_tnb.types._prelude.blob.deserialize_json(
            data["nsdContent"]
        )
    return out
