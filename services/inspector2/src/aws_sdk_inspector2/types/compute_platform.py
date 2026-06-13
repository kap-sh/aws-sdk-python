"""Generated from Smithy shape ``com.amazonaws.inspector2#ComputePlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.platform_version
    import aws_sdk_inspector2.types.product
    import aws_sdk_inspector2.types.vendor


class ComputePlatform(TypedDict):
    vendor: NotRequired["aws_sdk_inspector2.types.vendor.Vendor"]
    """<p>The compute platform vendor.</p>"""
    product: NotRequired["aws_sdk_inspector2.types.product.Product"]
    """<p>The compute platform product.</p>"""
    version: NotRequired["aws_sdk_inspector2.types.platform_version.PlatformVersion"]
    """<p>The compute platform version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputePlatform) -> dict:
    out: dict = {}
    if "vendor" in value:
        out["vendor"] = value["vendor"]
    if "product" in value:
        out["product"] = value["product"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ComputePlatform:
    out: ComputePlatform = {}  # type: ignore[typeddict-item]
    if "vendor" in data:
        out["vendor"] = data["vendor"]
    if "product" in data:
        out["product"] = data["product"]
    if "version" in data:
        out["version"] = data["version"]
    return out
