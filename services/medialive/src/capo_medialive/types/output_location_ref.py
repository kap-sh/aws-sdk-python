"""Generated from Smithy shape ``com.amazonaws.medialive#OutputLocationRef``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class OutputLocationRef(TypedDict, closed=True):
    destination_ref_id: NotRequired["capo_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputLocationRef) -> dict:
    out: dict = {}
    if "destination_ref_id" in value:
        out["destinationRefId"] = value["destination_ref_id"]
    return out


def deserialize_json(data: dict) -> OutputLocationRef:
    out: OutputLocationRef = {}  # type: ignore[typeddict-item]
    if "destinationRefId" in data:
        out["destination_ref_id"] = data["destinationRefId"]
    return out
