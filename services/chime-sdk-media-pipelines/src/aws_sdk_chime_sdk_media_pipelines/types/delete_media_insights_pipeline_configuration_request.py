"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#DeleteMediaInsightsPipelineConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class DeleteMediaInsightsPipelineConfigurationRequest(TypedDict):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the resource to be deleted. Valid values include the name and ARN of the media insights pipeline configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMediaInsightsPipelineConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMediaInsightsPipelineConfigurationRequest:
    out: DeleteMediaInsightsPipelineConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
