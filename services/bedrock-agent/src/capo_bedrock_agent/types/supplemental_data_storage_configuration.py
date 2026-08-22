"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupplementalDataStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.supplemental_data_storage_locations


class SupplementalDataStorageConfiguration(TypedDict, closed=True):
    storage_locations: "capo_bedrock_agent.types.supplemental_data_storage_locations.SupplementalDataStorageLocations"
    """<p>A list of objects specifying storage locations for images extracted from multimodal documents in your data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalDataStorageConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.supplemental_data_storage_locations

    out["storageLocations"] = (
        capo_bedrock_agent.types.supplemental_data_storage_locations.serialize_json(
            value["storage_locations"]
        )
    )
    return out


def deserialize_json(data: dict) -> SupplementalDataStorageConfiguration:
    out: SupplementalDataStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageLocations") is not None:
        import capo_bedrock_agent.types.supplemental_data_storage_locations

        out["storage_locations"] = (
            capo_bedrock_agent.types.supplemental_data_storage_locations.deserialize_json(
                data["storageLocations"]
            )
        )
    else:
        raise DeserializationError(
            "SupplementalDataStorageConfiguration.storage_locations required"
        )
    return out
