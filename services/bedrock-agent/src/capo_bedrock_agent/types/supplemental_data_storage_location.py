"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupplementalDataStorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.s3_location
    import capo_bedrock_agent.types.supplemental_data_storage_location_type


class SupplementalDataStorageLocation(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.supplemental_data_storage_location_type.SupplementalDataStorageLocationType"
    """<p>Specifies the storage service used for this location.</p>"""
    s3_location: NotRequired["capo_bedrock_agent.types.s3_location.S3Location"]
    """<p>Contains information about the Amazon S3 location for the extracted images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalDataStorageLocation) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.supplemental_data_storage_location_type

    out["type"] = (
        capo_bedrock_agent.types.supplemental_data_storage_location_type.serialize_json(
            value["type"]
        )
    )
    if "s3_location" in value:
        import capo_bedrock_agent.types.s3_location

        out["s3Location"] = capo_bedrock_agent.types.s3_location.serialize_json(
            value["s3_location"]
        )
    return out


def deserialize_json(data: dict) -> SupplementalDataStorageLocation:
    out: SupplementalDataStorageLocation = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock_agent.types.supplemental_data_storage_location_type

        out["type"] = (
            capo_bedrock_agent.types.supplemental_data_storage_location_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("SupplementalDataStorageLocation.type required")
    if "s3Location" in data:
        import capo_bedrock_agent.types.s3_location

        out["s3_location"] = capo_bedrock_agent.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    return out
