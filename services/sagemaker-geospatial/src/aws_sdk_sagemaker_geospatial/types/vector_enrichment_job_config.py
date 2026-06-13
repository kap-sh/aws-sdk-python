"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.map_matching_config
    import aws_sdk_sagemaker_geospatial.types.reverse_geocoding_config


class _VectorEnrichmentJobConfig_ReverseGeocodingConfig(TypedDict):
    ReverseGeocodingConfig: "aws_sdk_sagemaker_geospatial.types.reverse_geocoding_config.ReverseGeocodingConfig"


class _VectorEnrichmentJobConfig_MapMatchingConfig(TypedDict):
    MapMatchingConfig: (
        "aws_sdk_sagemaker_geospatial.types.map_matching_config.MapMatchingConfig"
    )


VectorEnrichmentJobConfig: TypeAlias = (
    _VectorEnrichmentJobConfig_ReverseGeocodingConfig
    | _VectorEnrichmentJobConfig_MapMatchingConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobConfig) -> dict:
    if "ReverseGeocodingConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.reverse_geocoding_config

        return {
            "ReverseGeocodingConfig": aws_sdk_sagemaker_geospatial.types.reverse_geocoding_config.serialize_json(
                value["ReverseGeocodingConfig"]
            )
        }
    elif "MapMatchingConfig" in value:
        import aws_sdk_sagemaker_geospatial.types.map_matching_config

        return {
            "MapMatchingConfig": aws_sdk_sagemaker_geospatial.types.map_matching_config.serialize_json(
                value["MapMatchingConfig"]
            )
        }
    else:
        raise SerializationError("VectorEnrichmentJobConfig: no variant present")


def deserialize_json(data: dict) -> VectorEnrichmentJobConfig:
    if "ReverseGeocodingConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.reverse_geocoding_config

        return {
            "ReverseGeocodingConfig": aws_sdk_sagemaker_geospatial.types.reverse_geocoding_config.deserialize_json(
                data["ReverseGeocodingConfig"]
            )
        }
    elif "MapMatchingConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.map_matching_config

        return {
            "MapMatchingConfig": aws_sdk_sagemaker_geospatial.types.map_matching_config.deserialize_json(
                data["MapMatchingConfig"]
            )
        }
    else:
        raise DeserializationError(
            "VectorEnrichmentJobConfig: no recognized variant key"
        )
