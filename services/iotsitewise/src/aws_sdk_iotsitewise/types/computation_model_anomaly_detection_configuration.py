"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelAnomalyDetectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.input_properties
    import aws_sdk_iotsitewise.types.result_property


class ComputationModelAnomalyDetectionConfiguration(TypedDict, closed=True):
    input_properties: "aws_sdk_iotsitewise.types.input_properties.InputProperties"
    """<p>Define the variable name associated with input properties, with the following format <code>${VariableName}</code>.</p>"""
    result_property: "aws_sdk_iotsitewise.types.result_property.ResultProperty"
    """<p>Define the variable name associated with the result property, and the following format <code>${VariableName}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelAnomalyDetectionConfiguration) -> dict:
    out: dict = {}
    out["inputProperties"] = value["input_properties"]
    out["resultProperty"] = value["result_property"]
    return out


def deserialize_json(data: dict) -> ComputationModelAnomalyDetectionConfiguration:
    out: ComputationModelAnomalyDetectionConfiguration = {}  # type: ignore[typeddict-item]
    if "inputProperties" in data:
        out["input_properties"] = data["inputProperties"]
    else:
        raise DeserializationError(
            "ComputationModelAnomalyDetectionConfiguration.input_properties required"
        )
    if "resultProperty" in data:
        out["result_property"] = data["resultProperty"]
    else:
        raise DeserializationError(
            "ComputationModelAnomalyDetectionConfiguration.result_property required"
        )
    return out
