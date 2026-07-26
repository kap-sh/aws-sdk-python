"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CompositedVideoConcatenationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state


class CompositedVideoConcatenationConfiguration(TypedDict, closed=True):
    state: "capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.ArtifactsConcatenationState"
    """<p>Enables or disables the configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompositedVideoConcatenationConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state

    out["State"] = (
        capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> CompositedVideoConcatenationConfiguration:
    out: CompositedVideoConcatenationConfiguration = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state

        out["state"] = (
            capo_chime_sdk_media_pipelines.types.artifacts_concatenation_state.deserialize_json(
                data["State"]
            )
        )
    else:
        raise DeserializationError(
            "CompositedVideoConcatenationConfiguration.state required"
        )
    return out
