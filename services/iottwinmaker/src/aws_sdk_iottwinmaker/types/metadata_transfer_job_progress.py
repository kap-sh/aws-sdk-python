"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#MetadataTransferJobProgress``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.integer


class MetadataTransferJobProgress(TypedDict):
    total_count: NotRequired["aws_sdk_iottwinmaker.types.integer.Integer"]
    """<p>The total count. [of what]</p>"""
    succeeded_count: NotRequired["aws_sdk_iottwinmaker.types.integer.Integer"]
    """<p>The succeeded count.</p>"""
    skipped_count: NotRequired["aws_sdk_iottwinmaker.types.integer.Integer"]
    """<p>The skipped count.</p>"""
    failed_count: NotRequired["aws_sdk_iottwinmaker.types.integer.Integer"]
    """<p>The failed count.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataTransferJobProgress) -> dict:
    out: dict = {}
    if "total_count" in value:
        out["totalCount"] = value["total_count"]
    if "succeeded_count" in value:
        out["succeededCount"] = value["succeeded_count"]
    if "skipped_count" in value:
        out["skippedCount"] = value["skipped_count"]
    if "failed_count" in value:
        out["failedCount"] = value["failed_count"]
    return out


def deserialize_json(data: dict) -> MetadataTransferJobProgress:
    out: MetadataTransferJobProgress = {}  # type: ignore[typeddict-item]
    if "totalCount" in data:
        out["total_count"] = data["totalCount"]
    if "succeededCount" in data:
        out["succeeded_count"] = data["succeededCount"]
    if "skippedCount" in data:
        out["skipped_count"] = data["skippedCount"]
    if "failedCount" in data:
        out["failed_count"] = data["failedCount"]
    return out
