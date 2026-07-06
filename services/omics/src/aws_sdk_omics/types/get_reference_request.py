"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.range
    import aws_sdk_omics.types.reference_file
    import aws_sdk_omics.types.reference_id
    import aws_sdk_omics.types.reference_store_id


class GetReferenceRequest(TypedDict, closed=True):
    id: "aws_sdk_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's store ID.</p>"""
    range: NotRequired["aws_sdk_omics.types.range.Range"]
    """<p>The range to retrieve.</p>"""
    part_number: "int"
    """<p>The part number to retrieve.</p>"""
    file: NotRequired["aws_sdk_omics.types.reference_file.ReferenceFile"]
    """<p>The file to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReferenceRequest:
    out: GetReferenceRequest = {}  # type: ignore[typeddict-item]
    return out
