"""Generated from Smithy shape ``com.amazonaws.iot#AwsJsonSubstitutionCommandPreprocessorConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.output_format


class AwsJsonSubstitutionCommandPreprocessorConfig(TypedDict):
    output_format: "aws_sdk_iot.types.output_format.OutputFormat"
    """<p>Converts the command preprocessor result to the format defined by this parameter, before sending it to the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJsonSubstitutionCommandPreprocessorConfig) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.output_format

    out["outputFormat"] = aws_sdk_iot.types.output_format.serialize_json(
        value["output_format"]
    )
    return out


def deserialize_json(data: dict) -> AwsJsonSubstitutionCommandPreprocessorConfig:
    out: AwsJsonSubstitutionCommandPreprocessorConfig = {}  # type: ignore[typeddict-item]
    if "outputFormat" in data:
        import aws_sdk_iot.types.output_format

        out["output_format"] = aws_sdk_iot.types.output_format.deserialize_json(
            data["outputFormat"]
        )
    else:
        raise DeserializationError(
            "AwsJsonSubstitutionCommandPreprocessorConfig.output_format required"
        )
    return out
