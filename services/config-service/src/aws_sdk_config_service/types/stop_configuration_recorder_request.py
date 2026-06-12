"""Generated from Smithy shape ``com.amazonaws.configservice#StopConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.recorder_name


class StopConfigurationRecorderRequest(TypedDict):
    configuration_recorder_name: (
        "aws_sdk_config_service.types.recorder_name.RecorderName"
    )
    """<p>The name of the customer managed configuration recorder that you want to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopConfigurationRecorderRequest) -> dict:
    out: dict = {}
    out["ConfigurationRecorderName"] = value["configuration_recorder_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopConfigurationRecorderRequest:
    out: StopConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorderName" in data:
        out["configuration_recorder_name"] = data["ConfigurationRecorderName"]
    else:
        raise DeserializationError(
            "StopConfigurationRecorderRequest.configuration_recorder_name required"
        )
    return out
