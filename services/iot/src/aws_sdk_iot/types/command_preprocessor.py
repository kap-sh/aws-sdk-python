"""Generated from Smithy shape ``com.amazonaws.iot#CommandPreprocessor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_json_substitution_command_preprocessor_config


class CommandPreprocessor(TypedDict):
    aws_json_substitution: NotRequired[
        "aws_sdk_iot.types.aws_json_substitution_command_preprocessor_config.AwsJsonSubstitutionCommandPreprocessorConfig"
    ]
    """<p>Configuration for the JSON substitution preprocessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandPreprocessor) -> dict:
    out: dict = {}
    if "aws_json_substitution" in value:
        import aws_sdk_iot.types.aws_json_substitution_command_preprocessor_config

        out["awsJsonSubstitution"] = (
            aws_sdk_iot.types.aws_json_substitution_command_preprocessor_config.serialize_json(
                value["aws_json_substitution"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommandPreprocessor:
    out: CommandPreprocessor = {}  # type: ignore[typeddict-item]
    if "awsJsonSubstitution" in data:
        import aws_sdk_iot.types.aws_json_substitution_command_preprocessor_config

        out["aws_json_substitution"] = (
            aws_sdk_iot.types.aws_json_substitution_command_preprocessor_config.deserialize_json(
                data["awsJsonSubstitution"]
            )
        )
    return out
