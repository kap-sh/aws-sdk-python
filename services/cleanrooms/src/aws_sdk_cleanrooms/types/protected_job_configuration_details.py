"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobConfigurationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_direct_analysis_configuration_details


class _ProtectedJobConfigurationDetails_directAnalysisConfigurationDetails(
    TypedDict, closed=True
):
    directAnalysisConfigurationDetails: "aws_sdk_cleanrooms.types.protected_job_direct_analysis_configuration_details.ProtectedJobDirectAnalysisConfigurationDetails"


ProtectedJobConfigurationDetails: TypeAlias = (
    _ProtectedJobConfigurationDetails_directAnalysisConfigurationDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobConfigurationDetails) -> dict:
    if "directAnalysisConfigurationDetails" in value:
        import aws_sdk_cleanrooms.types.protected_job_direct_analysis_configuration_details

        return {
            "directAnalysisConfigurationDetails": aws_sdk_cleanrooms.types.protected_job_direct_analysis_configuration_details.serialize_json(
                value["directAnalysisConfigurationDetails"]
            )
        }
    else:
        raise SerializationError("ProtectedJobConfigurationDetails: no variant present")


def deserialize_json(data: dict) -> ProtectedJobConfigurationDetails:
    if "directAnalysisConfigurationDetails" in data:
        import aws_sdk_cleanrooms.types.protected_job_direct_analysis_configuration_details

        return {
            "directAnalysisConfigurationDetails": aws_sdk_cleanrooms.types.protected_job_direct_analysis_configuration_details.deserialize_json(
                data["directAnalysisConfigurationDetails"]
            )
        }
    else:
        raise DeserializationError(
            "ProtectedJobConfigurationDetails: no recognized variant key"
        )
