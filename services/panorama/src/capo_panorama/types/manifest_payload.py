"""Generated from Smithy shape ``com.amazonaws.panorama#ManifestPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_panorama.types.manifest_payload_data


class _ManifestPayload_PayloadData(TypedDict, closed=True):
    PayloadData: "capo_panorama.types.manifest_payload_data.ManifestPayloadData"


ManifestPayload: TypeAlias = _ManifestPayload_PayloadData


# --- restJson1 ser/de ---
def serialize_json(value: ManifestPayload) -> dict:
    if "PayloadData" in value:
        return {"PayloadData": value["PayloadData"]}
    else:
        raise SerializationError("ManifestPayload: no variant present")


def deserialize_json(data: dict) -> ManifestPayload:
    if "PayloadData" in data:
        return {"PayloadData": data["PayloadData"]}
    else:
        raise DeserializationError("ManifestPayload: no recognized variant key")
