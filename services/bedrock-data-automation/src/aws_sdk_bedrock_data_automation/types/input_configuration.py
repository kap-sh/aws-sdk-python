"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.inline_payload
    import aws_sdk_bedrock_data_automation.types.s3_object


class InputConfiguration(TypedDict):
    s3_object: NotRequired["aws_sdk_bedrock_data_automation.types.s3_object.S3Object"]
    """S3 object"""
    inline_payload: NotRequired[
        "aws_sdk_bedrock_data_automation.types.inline_payload.InlinePayload"
    ]
    """Input Payload"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfiguration) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import aws_sdk_bedrock_data_automation.types.s3_object

        out["s3Object"] = (
            aws_sdk_bedrock_data_automation.types.s3_object.serialize_json(
                value["s3_object"]
            )
        )
    if "inline_payload" in value:
        import aws_sdk_bedrock_data_automation.types.inline_payload

        out["inlinePayload"] = (
            aws_sdk_bedrock_data_automation.types.inline_payload.serialize_json(
                value["inline_payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Object" in data:
        import aws_sdk_bedrock_data_automation.types.s3_object

        out["s3_object"] = (
            aws_sdk_bedrock_data_automation.types.s3_object.deserialize_json(
                data["s3Object"]
            )
        )
    if "inlinePayload" in data:
        import aws_sdk_bedrock_data_automation.types.inline_payload

        out["inline_payload"] = (
            aws_sdk_bedrock_data_automation.types.inline_payload.deserialize_json(
                data["inlinePayload"]
            )
        )
    return out
