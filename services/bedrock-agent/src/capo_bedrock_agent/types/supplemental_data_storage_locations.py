"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupplementalDataStorageLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.supplemental_data_storage_location

SupplementalDataStorageLocations: TypeAlias = list[
    "capo_bedrock_agent.types.supplemental_data_storage_location.SupplementalDataStorageLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalDataStorageLocations) -> list:
    import capo_bedrock_agent.types.supplemental_data_storage_location

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.supplemental_data_storage_location.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SupplementalDataStorageLocations:
    import capo_bedrock_agent.types.supplemental_data_storage_location

    out: SupplementalDataStorageLocations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.supplemental_data_storage_location.deserialize_json(
                item
            )
        )
    return out
