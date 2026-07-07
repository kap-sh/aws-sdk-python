"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentConcatenationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_state


class ContentConcatenationConfiguration(TypedDict, closed=True):
    state: "aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_state.ArtifactsConcatenationState"
    """<p>Enables or disables the configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentConcatenationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_state

    out["State"] = (
        aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContentConcatenationConfiguration:
    out: ContentConcatenationConfiguration = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_state

        out["state"] = (
            aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_state.deserialize_json(
                data["State"]
            )
        )
    else:
        raise DeserializationError("ContentConcatenationConfiguration.state required")
    return out
