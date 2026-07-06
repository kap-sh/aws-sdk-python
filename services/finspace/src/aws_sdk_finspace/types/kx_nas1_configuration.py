"""Generated from Smithy shape ``com.amazonaws.finspace#KxNAS1Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_nas1_size
    import aws_sdk_finspace.types.kx_nas1_type


class KxNAS1Configuration(TypedDict, closed=True):
    type: NotRequired["aws_sdk_finspace.types.kx_nas1_type.KxNAS1Type"]
    """<p> The type of the network attached storage. </p>"""
    size: NotRequired["aws_sdk_finspace.types.kx_nas1_size.KxNAS1Size"]
    """<p> The size of the network attached storage. For storage type <code>SSD_1000</code> and <code>SSD_250</code> you can select the minimum size as 1200 GB or increments of 2400 GB. For storage type <code>HDD_12</code> you can select the minimum size as 6000 GB or increments of 6000 GB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxNAS1Configuration) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_finspace.types.kx_nas1_type

        out["type"] = aws_sdk_finspace.types.kx_nas1_type.serialize_json(value["type"])
    if "size" in value:
        out["size"] = value["size"]
    return out


def deserialize_json(data: dict) -> KxNAS1Configuration:
    out: KxNAS1Configuration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_finspace.types.kx_nas1_type

        out["type"] = aws_sdk_finspace.types.kx_nas1_type.deserialize_json(data["type"])
    if "size" in data:
        out["size"] = data["size"]
    return out
