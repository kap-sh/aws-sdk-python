"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobReceiverConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_analysis_type
    import aws_sdk_cleanrooms.types.protected_job_configuration_details


class ProtectedJobReceiverConfiguration(TypedDict):
    analysis_type: (
        "aws_sdk_cleanrooms.types.protected_job_analysis_type.ProtectedJobAnalysisType"
    )
    """<p> The analysis type for the protected job receiver configuration.</p>"""
    configuration_details: NotRequired[
        "aws_sdk_cleanrooms.types.protected_job_configuration_details.ProtectedJobConfigurationDetails"
    ]
    """<p> The configuration details for the protected job receiver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobReceiverConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job_analysis_type

    out["analysisType"] = (
        aws_sdk_cleanrooms.types.protected_job_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    if "configuration_details" in value:
        import aws_sdk_cleanrooms.types.protected_job_configuration_details

        out["configurationDetails"] = (
            aws_sdk_cleanrooms.types.protected_job_configuration_details.serialize_json(
                value["configuration_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobReceiverConfiguration:
    out: ProtectedJobReceiverConfiguration = {}  # type: ignore[typeddict-item]
    if "analysisType" in data:
        import aws_sdk_cleanrooms.types.protected_job_analysis_type

        out["analysis_type"] = (
            aws_sdk_cleanrooms.types.protected_job_analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedJobReceiverConfiguration.analysis_type required"
        )
    if "configurationDetails" in data:
        import aws_sdk_cleanrooms.types.protected_job_configuration_details

        out["configuration_details"] = (
            aws_sdk_cleanrooms.types.protected_job_configuration_details.deserialize_json(
                data["configurationDetails"]
            )
        )
    return out
