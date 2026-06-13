"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ReceiverConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_type
    import aws_sdk_cleanrooms.types.configuration_details


class ReceiverConfiguration(TypedDict):
    analysis_type: "aws_sdk_cleanrooms.types.analysis_type.AnalysisType"
    """<p> The type of analysis for the protected query. The results of the query can be analyzed directly (<code>DIRECT_ANALYSIS</code>) or used as input into additional analyses (<code>ADDITIONAL_ANALYSIS</code>), such as a query that is a seed for a lookalike ML model.</p>"""
    configuration_details: NotRequired[
        "aws_sdk_cleanrooms.types.configuration_details.ConfigurationDetails"
    ]
    """<p> The configuration details of the receiver configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReceiverConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_type

    out["analysisType"] = aws_sdk_cleanrooms.types.analysis_type.serialize_json(
        value["analysis_type"]
    )
    if "configuration_details" in value:
        import aws_sdk_cleanrooms.types.configuration_details

        out["configurationDetails"] = (
            aws_sdk_cleanrooms.types.configuration_details.serialize_json(
                value["configuration_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReceiverConfiguration:
    out: ReceiverConfiguration = {}  # type: ignore[typeddict-item]
    if "analysisType" in data:
        import aws_sdk_cleanrooms.types.analysis_type

        out["analysis_type"] = aws_sdk_cleanrooms.types.analysis_type.deserialize_json(
            data["analysisType"]
        )
    else:
        raise DeserializationError("ReceiverConfiguration.analysis_type required")
    if "configurationDetails" in data:
        import aws_sdk_cleanrooms.types.configuration_details

        out["configuration_details"] = (
            aws_sdk_cleanrooms.types.configuration_details.deserialize_json(
                data["configurationDetails"]
            )
        )
    return out
