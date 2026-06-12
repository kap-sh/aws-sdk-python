"""Generated from Smithy shape ``com.amazonaws.ivs#GetRecordingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.recording_configuration_arn


class GetRecordingConfigurationRequest(TypedDict):
    arn: "aws_sdk_ivs.types.recording_configuration_arn.RecordingConfigurationArn"
    """<p>ARN of the recording configuration to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecordingConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetRecordingConfigurationRequest:
    out: GetRecordingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetRecordingConfigurationRequest.arn required")
    return out
