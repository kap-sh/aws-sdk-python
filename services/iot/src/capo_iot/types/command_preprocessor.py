"""Generated from Smithy shape ``com.amazonaws.iot#CommandPreprocessor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_json_substitution_command_preprocessor_config


class CommandPreprocessor(TypedDict, closed=True):
    aws_json_substitution: NotRequired[
        "capo_iot.types.aws_json_substitution_command_preprocessor_config.AwsJsonSubstitutionCommandPreprocessorConfig"
    ]
    """<p>Configuration for the JSON substitution preprocessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandPreprocessor) -> dict:
    out: dict = {}
    if "aws_json_substitution" in value:
        import capo_iot.types.aws_json_substitution_command_preprocessor_config

        out["awsJsonSubstitution"] = (
            capo_iot.types.aws_json_substitution_command_preprocessor_config.serialize_json(
                value["aws_json_substitution"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommandPreprocessor:
    out: CommandPreprocessor = {}  # type: ignore[typeddict-item]
    if "awsJsonSubstitution" in data:
        import capo_iot.types.aws_json_substitution_command_preprocessor_config

        out["aws_json_substitution"] = (
            capo_iot.types.aws_json_substitution_command_preprocessor_config.deserialize_json(
                data["awsJsonSubstitution"]
            )
        )
    return out
