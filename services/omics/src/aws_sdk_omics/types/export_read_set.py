"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_id


class ExportReadSet(TypedDict, closed=True):
    read_set_id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The set's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSet) -> dict:
    out: dict = {}
    out["readSetId"] = value["read_set_id"]
    return out


def deserialize_json(data: dict) -> ExportReadSet:
    out: ExportReadSet = {}  # type: ignore[typeddict-item]
    if "readSetId" in data:
        out["read_set_id"] = data["readSetId"]
    else:
        raise DeserializationError("ExportReadSet.read_set_id required")
    return out
