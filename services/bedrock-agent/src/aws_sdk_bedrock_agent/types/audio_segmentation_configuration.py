"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AudioSegmentationConfiguration``."""

from typing import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError


class AudioSegmentationConfiguration(TypedDict):
    fixed_length_duration: "int"
    """<p>The duration in seconds for each audio segment. Audio files will be divided into chunks of this length for processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSegmentationConfiguration) -> dict:
    out: dict = {}
    out["fixedLengthDuration"] = value["fixed_length_duration"]
    return out


def deserialize_json(data: dict) -> AudioSegmentationConfiguration:
    out: AudioSegmentationConfiguration = {}  # type: ignore[typeddict-item]
    if "fixedLengthDuration" in data:
        out["fixed_length_duration"] = data["fixedLengthDuration"]
    else:
        raise DeserializationError(
            "AudioSegmentationConfiguration.fixed_length_duration required"
        )
    return out
