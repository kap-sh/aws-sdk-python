"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaInsightsPipelineConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class GetMediaInsightsPipelineConfigurationRequest(TypedDict):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the requested resource. Valid values include the name and ARN of the media insights pipeline configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaInsightsPipelineConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMediaInsightsPipelineConfigurationRequest:
    out: GetMediaInsightsPipelineConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
