"""Generated from Smithy shape ``com.amazonaws.braket#AlgorithmSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_braket.types.container_image
    import aws_sdk_braket.types.script_mode_config


class AlgorithmSpecification(TypedDict):
    script_mode_config: NotRequired[
        "aws_sdk_braket.types.script_mode_config.ScriptModeConfig"
    ]
    """<p>Configures the paths to the Python scripts used for entry and training.</p>"""
    container_image: NotRequired["aws_sdk_braket.types.container_image.ContainerImage"]
    """<p>The container image used to create an Amazon Braket hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlgorithmSpecification) -> dict:
    out: dict = {}
    if "script_mode_config" in value:
        import aws_sdk_braket.types.script_mode_config

        out["scriptModeConfig"] = (
            aws_sdk_braket.types.script_mode_config.serialize_json(
                value["script_mode_config"]
            )
        )
    if "container_image" in value:
        import aws_sdk_braket.types.container_image

        out["containerImage"] = aws_sdk_braket.types.container_image.serialize_json(
            value["container_image"]
        )
    return out


def deserialize_json(data: dict) -> AlgorithmSpecification:
    out: AlgorithmSpecification = {}  # type: ignore[typeddict-item]
    if "scriptModeConfig" in data:
        import aws_sdk_braket.types.script_mode_config

        out["script_mode_config"] = (
            aws_sdk_braket.types.script_mode_config.deserialize_json(
                data["scriptModeConfig"]
            )
        )
    if "containerImage" in data:
        import aws_sdk_braket.types.container_image

        out["container_image"] = aws_sdk_braket.types.container_image.deserialize_json(
            data["containerImage"]
        )
    return out
