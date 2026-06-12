"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackInputParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.parameter_name
    import aws_sdk_config_service.types.parameter_value


class ConformancePackInputParameter(TypedDict):
    parameter_name: "aws_sdk_config_service.types.parameter_name.ParameterName"
    """<p>One part of a key-value pair.</p>"""
    parameter_value: "aws_sdk_config_service.types.parameter_value.ParameterValue"
    """<p>Another part of the key-value pair. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackInputParameter) -> dict:
    out: dict = {}
    out["ParameterName"] = value["parameter_name"]
    out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackInputParameter:
    out: ConformancePackInputParameter = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    else:
        raise DeserializationError(
            "ConformancePackInputParameter.parameter_name required"
        )
    if "ParameterValue" in data:
        out["parameter_value"] = data["ParameterValue"]
    else:
        raise DeserializationError(
            "ConformancePackInputParameter.parameter_value required"
        )
    return out
