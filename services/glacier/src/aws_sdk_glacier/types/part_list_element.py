"""Generated from Smithy shape ``com.amazonaws.glacier#PartListElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class PartListElement(TypedDict):
    range_in_bytes: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The byte range of a part, inclusive of the upper value of the range.</p>"""
    sha256_tree_hash: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The SHA256 tree hash value that Amazon Glacier calculated for the part. This field is never <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartListElement) -> dict:
    out: dict = {}
    if "range_in_bytes" in value:
        out["RangeInBytes"] = value["range_in_bytes"]
    if "sha256_tree_hash" in value:
        out["SHA256TreeHash"] = value["sha256_tree_hash"]
    return out


def deserialize_json(data: dict) -> PartListElement:
    out: PartListElement = {}  # type: ignore[typeddict-item]
    if "RangeInBytes" in data:
        out["range_in_bytes"] = data["RangeInBytes"]
    if "SHA256TreeHash" in data:
        out["sha256_tree_hash"] = data["SHA256TreeHash"]
    return out
