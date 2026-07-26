"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CompositedVideoArtifactsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.grid_view_configuration
    import capo_chime_sdk_media_pipelines.types.layout_option
    import capo_chime_sdk_media_pipelines.types.resolution_option


class CompositedVideoArtifactsConfiguration(TypedDict, closed=True):
    layout: NotRequired[
        "capo_chime_sdk_media_pipelines.types.layout_option.LayoutOption"
    ]
    """<p>The layout setting, such as <code>GridView</code> in the configuration object.</p>"""
    resolution: NotRequired[
        "capo_chime_sdk_media_pipelines.types.resolution_option.ResolutionOption"
    ]
    """<p>The video resolution setting in the configuration object. Default: HD at 1280 x 720. FHD resolution: 1920 x 1080.</p>"""
    grid_view_configuration: "capo_chime_sdk_media_pipelines.types.grid_view_configuration.GridViewConfiguration"
    """<p>The <code>GridView</code> configuration setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositedVideoArtifactsConfiguration) -> dict:
    out: dict = {}
    if "layout" in value:
        import capo_chime_sdk_media_pipelines.types.layout_option

        out["Layout"] = (
            capo_chime_sdk_media_pipelines.types.layout_option.serialize_json(
                value["layout"]
            )
        )
    if "resolution" in value:
        import capo_chime_sdk_media_pipelines.types.resolution_option

        out["Resolution"] = (
            capo_chime_sdk_media_pipelines.types.resolution_option.serialize_json(
                value["resolution"]
            )
        )
    import capo_chime_sdk_media_pipelines.types.grid_view_configuration

    out["GridViewConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.grid_view_configuration.serialize_json(
            value["grid_view_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CompositedVideoArtifactsConfiguration:
    out: CompositedVideoArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if "Layout" in data:
        import capo_chime_sdk_media_pipelines.types.layout_option

        out["layout"] = (
            capo_chime_sdk_media_pipelines.types.layout_option.deserialize_json(
                data["Layout"]
            )
        )
    if "Resolution" in data:
        import capo_chime_sdk_media_pipelines.types.resolution_option

        out["resolution"] = (
            capo_chime_sdk_media_pipelines.types.resolution_option.deserialize_json(
                data["Resolution"]
            )
        )
    if "GridViewConfiguration" in data:
        import capo_chime_sdk_media_pipelines.types.grid_view_configuration

        out["grid_view_configuration"] = (
            capo_chime_sdk_media_pipelines.types.grid_view_configuration.deserialize_json(
                data["GridViewConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CompositedVideoArtifactsConfiguration.grid_view_configuration required"
        )
    return out
