"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.recorder_name


class DeleteConfigurationRecorderRequest(TypedDict):
    configuration_recorder_name: (
        "aws_sdk_config_service.types.recorder_name.RecorderName"
    )
    """<p>The name of the customer managed configuration recorder that you want to delete. You can retrieve the name of your configuration recorders by using the <a href=\"https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html\">DescribeConfigurationRecorders</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConfigurationRecorderRequest) -> dict:
    out: dict = {}
    out["ConfigurationRecorderName"] = value["configuration_recorder_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConfigurationRecorderRequest:
    out: DeleteConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorderName" in data:
        out["configuration_recorder_name"] = data["ConfigurationRecorderName"]
    else:
        raise DeserializationError(
            "DeleteConfigurationRecorderRequest.configuration_recorder_name required"
        )
    return out
