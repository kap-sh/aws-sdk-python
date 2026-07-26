"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineElementStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type
    import capo_chime_sdk_media_pipelines.types.media_pipeline_element_status


class MediaInsightsPipelineElementStatus(TypedDict, closed=True):
    type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.MediaInsightsPipelineConfigurationElementType"
    ]
    """<p>The type of status.</p>"""
    status: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_element_status.MediaPipelineElementStatus"
    ]
    """<p>The element's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineElementStatus) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type

        out["Type"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.serialize_json(
                value["type"]
            )
        )
    if "status" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_element_status

        out["Status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_element_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaInsightsPipelineElementStatus:
    out: MediaInsightsPipelineElementStatus = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type

        out["type"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element_type.deserialize_json(
                data["Type"]
            )
        )
    if "Status" in data:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_element_status

        out["status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_element_status.deserialize_json(
                data["Status"]
            )
        )
    return out
