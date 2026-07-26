"""Generated from Smithy shape ``com.amazonaws.omics#UploadReadSetPartResponse``."""

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError


class UploadReadSetPartResponse(TypedDict, closed=True):
    checksum: "str"
    """<p>An identifier used to confirm that parts are being added to the intended upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadReadSetPartResponse) -> dict:
    out: dict = {}
    out["checksum"] = value["checksum"]
    return out


def deserialize_json(data: dict) -> UploadReadSetPartResponse:
    out: UploadReadSetPartResponse = {}  # type: ignore[typeddict-item]
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    else:
        raise DeserializationError("UploadReadSetPartResponse.checksum required")
    return out
