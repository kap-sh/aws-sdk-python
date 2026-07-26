"""Generated from Smithy shape ``com.amazonaws.omics#CompleteReadSetUploadPartListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.read_set_part_source


class CompleteReadSetUploadPartListItem(TypedDict, closed=True):
    part_number: "int"
    """<p> A number identifying the part in a read set upload. </p>"""
    part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource"
    """<p> The source file of the part being uploaded. </p>"""
    checksum: "str"
    """<p> A unique identifier used to confirm that parts are being added to the correct upload. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteReadSetUploadPartListItem) -> dict:
    out: dict = {}
    out["partNumber"] = value["part_number"]
    out["partSource"] = value["part_source"]
    out["checksum"] = value["checksum"]
    return out


def deserialize_json(data: dict) -> CompleteReadSetUploadPartListItem:
    out: CompleteReadSetUploadPartListItem = {}  # type: ignore[typeddict-item]
    if "partNumber" in data:
        out["part_number"] = data["partNumber"]
    else:
        raise DeserializationError(
            "CompleteReadSetUploadPartListItem.part_number required"
        )
    if "partSource" in data:
        out["part_source"] = data["partSource"]
    else:
        raise DeserializationError(
            "CompleteReadSetUploadPartListItem.part_source required"
        )
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    else:
        raise DeserializationError(
            "CompleteReadSetUploadPartListItem.checksum required"
        )
    return out
