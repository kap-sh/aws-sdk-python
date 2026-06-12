"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardGenerativeField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.state
    import aws_sdk_bedrock_data_automation.types.video_standard_generative_field_types


class VideoStandardGenerativeField(TypedDict):
    state: "aws_sdk_bedrock_data_automation.types.state.State"
    types: NotRequired[
        "aws_sdk_bedrock_data_automation.types.video_standard_generative_field_types.VideoStandardGenerativeFieldTypes"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VideoStandardGenerativeField) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.state

    out["state"] = aws_sdk_bedrock_data_automation.types.state.serialize_json(
        value["state"]
    )
    if "types" in value:
        import aws_sdk_bedrock_data_automation.types.video_standard_generative_field_types

        out["types"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_generative_field_types.serialize_json(
                value["types"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoStandardGenerativeField:
    out: VideoStandardGenerativeField = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_bedrock_data_automation.types.state

        out["state"] = aws_sdk_bedrock_data_automation.types.state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("VideoStandardGenerativeField.state required")
    if "types" in data:
        import aws_sdk_bedrock_data_automation.types.video_standard_generative_field_types

        out["types"] = (
            aws_sdk_bedrock_data_automation.types.video_standard_generative_field_types.deserialize_json(
                data["types"]
            )
        )
    return out
