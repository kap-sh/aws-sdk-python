"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobReceiverConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_analysis_type
    import capo_cleanrooms.types.protected_job_configuration_details


class ProtectedJobReceiverConfiguration(TypedDict, closed=True):
    analysis_type: (
        "capo_cleanrooms.types.protected_job_analysis_type.ProtectedJobAnalysisType"
    )
    """<p> The analysis type for the protected job receiver configuration.</p>"""
    configuration_details: NotRequired[
        "capo_cleanrooms.types.protected_job_configuration_details.ProtectedJobConfigurationDetails"
    ]
    """<p> The configuration details for the protected job receiver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobReceiverConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job_analysis_type

    out["analysisType"] = (
        capo_cleanrooms.types.protected_job_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    if "configuration_details" in value:
        import capo_cleanrooms.types.protected_job_configuration_details

        out["configurationDetails"] = (
            capo_cleanrooms.types.protected_job_configuration_details.serialize_json(
                value["configuration_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobReceiverConfiguration:
    out: ProtectedJobReceiverConfiguration = {}  # type: ignore[typeddict-item]
    if "analysisType" in data:
        import capo_cleanrooms.types.protected_job_analysis_type

        out["analysis_type"] = (
            capo_cleanrooms.types.protected_job_analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedJobReceiverConfiguration.analysis_type required"
        )
    if "configurationDetails" in data:
        import capo_cleanrooms.types.protected_job_configuration_details

        out["configuration_details"] = (
            capo_cleanrooms.types.protected_job_configuration_details.deserialize_json(
                data["configurationDetails"]
            )
        )
    return out
