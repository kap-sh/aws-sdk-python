"""Generated from Smithy shape ``com.amazonaws.panorama#ManifestOverridesPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_panorama.types.manifest_overrides_payload_data


class _ManifestOverridesPayload_PayloadData(TypedDict, closed=True):
    PayloadData: "capo_panorama.types.manifest_overrides_payload_data.ManifestOverridesPayloadData"


ManifestOverridesPayload: TypeAlias = _ManifestOverridesPayload_PayloadData


# --- restJson1 ser/de ---
def serialize_json(value: ManifestOverridesPayload) -> dict:
    if "PayloadData" in value:
        return {"PayloadData": value["PayloadData"]}
    else:
        raise SerializationError("ManifestOverridesPayload: no variant present")


def deserialize_json(data: dict) -> ManifestOverridesPayload:
    if "PayloadData" in data:
        return {"PayloadData": data["PayloadData"]}
    else:
        raise DeserializationError(
            "ManifestOverridesPayload: no recognized variant key"
        )
