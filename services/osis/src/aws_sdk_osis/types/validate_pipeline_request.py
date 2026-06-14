"""Generated from Smithy shape ``com.amazonaws.osis#ValidatePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_osis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_configuration_body


class ValidatePipelineRequest(TypedDict):
    pipeline_configuration_body: (
        "aws_sdk_osis.types.pipeline_configuration_body.PipelineConfigurationBody"
    )
    r"""<p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePipelineRequest) -> dict:
    out: dict = {}
    out["PipelineConfigurationBody"] = value["pipeline_configuration_body"]
    return out


def deserialize_json(data: dict) -> ValidatePipelineRequest:
    out: ValidatePipelineRequest = {}  # type: ignore[typeddict-item]
    if "PipelineConfigurationBody" in data:
        out["pipeline_configuration_body"] = data["PipelineConfigurationBody"]
    else:
        raise DeserializationError(
            "ValidatePipelineRequest.pipeline_configuration_body required"
        )
    return out
