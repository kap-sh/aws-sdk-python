"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SamplingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.sampling_percentage


class SamplingConfig(TypedDict, closed=True):
    sampling_percentage: (
        "aws_sdk_bedrock_agentcore_control.types.sampling_percentage.SamplingPercentage"
    )
    """<p> The percentage of agent traces to sample for evaluation, ranging from 0.01% to 100%. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingConfig) -> dict:
    out: dict = {}
    out["samplingPercentage"] = value["sampling_percentage"]
    return out


def deserialize_json(data: dict) -> SamplingConfig:
    out: SamplingConfig = {}  # type: ignore[typeddict-item]
    if "samplingPercentage" in data:
        out["sampling_percentage"] = data["samplingPercentage"]
    else:
        raise DeserializationError("SamplingConfig.sampling_percentage required")
    return out
