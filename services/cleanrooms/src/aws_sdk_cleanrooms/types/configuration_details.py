"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfigurationDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.direct_analysis_configuration_details


class _ConfigurationDetails_directAnalysisConfigurationDetails(TypedDict):
    directAnalysisConfigurationDetails: "aws_sdk_cleanrooms.types.direct_analysis_configuration_details.DirectAnalysisConfigurationDetails"


ConfigurationDetails: TypeAlias = (
    _ConfigurationDetails_directAnalysisConfigurationDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDetails) -> dict:
    if "directAnalysisConfigurationDetails" in value:
        import aws_sdk_cleanrooms.types.direct_analysis_configuration_details

        return {
            "directAnalysisConfigurationDetails": aws_sdk_cleanrooms.types.direct_analysis_configuration_details.serialize_json(
                value["directAnalysisConfigurationDetails"]
            )
        }
    else:
        raise SerializationError("ConfigurationDetails: no variant present")


def deserialize_json(data: dict) -> ConfigurationDetails:
    if "directAnalysisConfigurationDetails" in data:
        import aws_sdk_cleanrooms.types.direct_analysis_configuration_details

        return {
            "directAnalysisConfigurationDetails": aws_sdk_cleanrooms.types.direct_analysis_configuration_details.deserialize_json(
                data["directAnalysisConfigurationDetails"]
            )
        }
    else:
        raise DeserializationError("ConfigurationDetails: no recognized variant key")
