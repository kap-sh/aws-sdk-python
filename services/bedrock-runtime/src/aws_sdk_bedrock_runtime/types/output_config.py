"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.output_format


class OutputConfig(TypedDict):
    text_format: NotRequired["aws_sdk_bedrock_runtime.types.output_format.OutputFormat"]
    """<p>Structured output parameters to control the model's text response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfig) -> dict:
    out: dict = {}
    if "text_format" in value:
        import aws_sdk_bedrock_runtime.types.output_format

        out["textFormat"] = aws_sdk_bedrock_runtime.types.output_format.serialize_json(
            value["text_format"]
        )
    return out


def deserialize_json(data: dict) -> OutputConfig:
    out: OutputConfig = {}  # type: ignore[typeddict-item]
    if "textFormat" in data:
        import aws_sdk_bedrock_runtime.types.output_format

        out["text_format"] = (
            aws_sdk_bedrock_runtime.types.output_format.deserialize_json(
                data["textFormat"]
            )
        )
    return out
