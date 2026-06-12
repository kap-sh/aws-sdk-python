"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ChannelLabelingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.state


class ChannelLabelingConfiguration(TypedDict):
    state: "aws_sdk_bedrock_data_automation.types.state.State"


# --- restJson1 ser/de ---
def serialize_json(value: ChannelLabelingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.state

    out["state"] = aws_sdk_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> ChannelLabelingConfiguration:
    out: ChannelLabelingConfiguration = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_bedrock_data_automation.types.state

        out["state"] = aws_sdk_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("ChannelLabelingConfiguration.state required")
    return out
