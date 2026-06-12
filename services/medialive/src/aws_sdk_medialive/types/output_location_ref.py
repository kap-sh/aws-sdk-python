"""Generated from Smithy shape ``com.amazonaws.medialive#OutputLocationRef``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class OutputLocationRef(TypedDict):
    destination_ref_id: NotRequired["aws_sdk_medialive.types.__string.__string"]


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
