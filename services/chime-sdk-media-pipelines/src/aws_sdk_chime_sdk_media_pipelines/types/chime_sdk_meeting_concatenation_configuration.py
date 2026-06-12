"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ChimeSdkMeetingConcatenationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_configuration


class ChimeSdkMeetingConcatenationConfiguration(TypedDict):
    artifacts_configuration: "aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_configuration.ArtifactsConcatenationConfiguration"
    """<p>The configuration for the artifacts in an Amazon Chime SDK meeting concatenation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChimeSdkMeetingConcatenationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_configuration

    out["ArtifactsConfiguration"] = (
        aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_configuration.serialize_json(
            value["artifacts_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChimeSdkMeetingConcatenationConfiguration:
    out: ChimeSdkMeetingConcatenationConfiguration = {}  # type: ignore[typeddict-item]
    if "ArtifactsConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_configuration

        out["artifacts_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.artifacts_concatenation_configuration.deserialize_json(
                data["ArtifactsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ChimeSdkMeetingConcatenationConfiguration.artifacts_configuration required"
        )
    return out
