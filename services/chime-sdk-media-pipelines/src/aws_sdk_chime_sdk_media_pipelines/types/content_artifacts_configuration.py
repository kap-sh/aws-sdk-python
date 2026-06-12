"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentArtifactsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.artifacts_state
    import aws_sdk_chime_sdk_media_pipelines.types.content_mux_type


class ContentArtifactsConfiguration(TypedDict):
    state: "aws_sdk_chime_sdk_media_pipelines.types.artifacts_state.ArtifactsState"
    """<p>Indicates whether the content artifact is enabled or disabled.</p>"""
    mux_type: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.content_mux_type.ContentMuxType"
    ]
    """<p>The MUX type of the artifact configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentArtifactsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.artifacts_state

    out["State"] = (
        aws_sdk_chime_sdk_media_pipelines.types.artifacts_state.serialize_json(
            value["state"]
        )
    )
    if "mux_type" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.content_mux_type

        out["MuxType"] = (
            aws_sdk_chime_sdk_media_pipelines.types.content_mux_type.serialize_json(
                value["mux_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentArtifactsConfiguration:
    out: ContentArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.artifacts_state

        out["state"] = (
            aws_sdk_chime_sdk_media_pipelines.types.artifacts_state.deserialize_json(
                data["State"]
            )
        )
    else:
        raise DeserializationError("ContentArtifactsConfiguration.state required")
    if "MuxType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.content_mux_type

        out["mux_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.content_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    return out
