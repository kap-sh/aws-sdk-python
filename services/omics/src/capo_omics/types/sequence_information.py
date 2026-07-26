"""Generated from Smithy shape ``com.amazonaws.omics#SequenceInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.generated_from


class SequenceInformation(TypedDict, closed=True):
    total_read_count: NotRequired["int"]
    """<p>The sequence's total read count.</p>"""
    total_base_count: NotRequired["int"]
    """<p>The sequence's total base count.</p>"""
    generated_from: NotRequired["capo_omics.types.generated_from.GeneratedFrom"]
    """<p>Where the sequence originated.</p>"""
    alignment: NotRequired["str"]
    """<p>The sequence's alignment setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SequenceInformation) -> dict:
    out: dict = {}
    if "total_read_count" in value:
        out["totalReadCount"] = value["total_read_count"]
    if "total_base_count" in value:
        out["totalBaseCount"] = value["total_base_count"]
    if "generated_from" in value:
        out["generatedFrom"] = value["generated_from"]
    if "alignment" in value:
        out["alignment"] = value["alignment"]
    return out


def deserialize_json(data: dict) -> SequenceInformation:
    out: SequenceInformation = {}  # type: ignore[typeddict-item]
    if "totalReadCount" in data:
        out["total_read_count"] = data["totalReadCount"]
    if "totalBaseCount" in data:
        out["total_base_count"] = data["totalBaseCount"]
    if "generatedFrom" in data:
        out["generated_from"] = data["generatedFrom"]
    if "alignment" in data:
        out["alignment"] = data["alignment"]
    return out
