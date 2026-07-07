"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GridViewConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.active_speaker_only_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.canvas_orientation
    import aws_sdk_chime_sdk_media_pipelines.types.content_share_layout_option
    import aws_sdk_chime_sdk_media_pipelines.types.horizontal_layout_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.presenter_only_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.vertical_layout_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.video_attribute


class GridViewConfiguration(TypedDict, closed=True):
    content_share_layout: "aws_sdk_chime_sdk_media_pipelines.types.content_share_layout_option.ContentShareLayoutOption"
    """<p>Defines the layout of the video tiles when content sharing is enabled.</p>"""
    presenter_only_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.presenter_only_configuration.PresenterOnlyConfiguration"
    ]
    """<p>Defines the configuration options for a presenter only video tile.</p>"""
    active_speaker_only_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.active_speaker_only_configuration.ActiveSpeakerOnlyConfiguration"
    ]
    """<p>The configuration settings for an <code>ActiveSpeakerOnly</code> video tile.</p>"""
    horizontal_layout_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.horizontal_layout_configuration.HorizontalLayoutConfiguration"
    ]
    """<p>The configuration settings for a horizontal layout.</p>"""
    vertical_layout_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.vertical_layout_configuration.VerticalLayoutConfiguration"
    ]
    """<p>The configuration settings for a vertical layout.</p>"""
    video_attribute: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.video_attribute.VideoAttribute"
    ]
    """<p>The attribute settings for the video tiles.</p>"""
    canvas_orientation: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.canvas_orientation.CanvasOrientation"
    ]
    """<p>The orientation setting, horizontal or vertical.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridViewConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.content_share_layout_option

    out["ContentShareLayout"] = (
        aws_sdk_chime_sdk_media_pipelines.types.content_share_layout_option.serialize_json(
            value["content_share_layout"]
        )
    )
    if "presenter_only_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.presenter_only_configuration

        out["PresenterOnlyConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.presenter_only_configuration.serialize_json(
                value["presenter_only_configuration"]
            )
        )
    if "active_speaker_only_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.active_speaker_only_configuration

        out["ActiveSpeakerOnlyConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.active_speaker_only_configuration.serialize_json(
                value["active_speaker_only_configuration"]
            )
        )
    if "horizontal_layout_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.horizontal_layout_configuration

        out["HorizontalLayoutConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.horizontal_layout_configuration.serialize_json(
                value["horizontal_layout_configuration"]
            )
        )
    if "vertical_layout_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.vertical_layout_configuration

        out["VerticalLayoutConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.vertical_layout_configuration.serialize_json(
                value["vertical_layout_configuration"]
            )
        )
    if "video_attribute" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.video_attribute

        out["VideoAttribute"] = (
            aws_sdk_chime_sdk_media_pipelines.types.video_attribute.serialize_json(
                value["video_attribute"]
            )
        )
    if "canvas_orientation" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.canvas_orientation

        out["CanvasOrientation"] = (
            aws_sdk_chime_sdk_media_pipelines.types.canvas_orientation.serialize_json(
                value["canvas_orientation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GridViewConfiguration:
    out: GridViewConfiguration = {}  # type: ignore[typeddict-item]
    if "ContentShareLayout" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.content_share_layout_option

        out["content_share_layout"] = (
            aws_sdk_chime_sdk_media_pipelines.types.content_share_layout_option.deserialize_json(
                data["ContentShareLayout"]
            )
        )
    else:
        raise DeserializationError(
            "GridViewConfiguration.content_share_layout required"
        )
    if "PresenterOnlyConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.presenter_only_configuration

        out["presenter_only_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.presenter_only_configuration.deserialize_json(
                data["PresenterOnlyConfiguration"]
            )
        )
    if "ActiveSpeakerOnlyConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.active_speaker_only_configuration

        out["active_speaker_only_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.active_speaker_only_configuration.deserialize_json(
                data["ActiveSpeakerOnlyConfiguration"]
            )
        )
    if "HorizontalLayoutConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.horizontal_layout_configuration

        out["horizontal_layout_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.horizontal_layout_configuration.deserialize_json(
                data["HorizontalLayoutConfiguration"]
            )
        )
    if "VerticalLayoutConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.vertical_layout_configuration

        out["vertical_layout_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.vertical_layout_configuration.deserialize_json(
                data["VerticalLayoutConfiguration"]
            )
        )
    if "VideoAttribute" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.video_attribute

        out["video_attribute"] = (
            aws_sdk_chime_sdk_media_pipelines.types.video_attribute.deserialize_json(
                data["VideoAttribute"]
            )
        )
    if "CanvasOrientation" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.canvas_orientation

        out["canvas_orientation"] = (
            aws_sdk_chime_sdk_media_pipelines.types.canvas_orientation.deserialize_json(
                data["CanvasOrientation"]
            )
        )
    return out
