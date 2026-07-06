"""Generated from Smithy shape ``com.amazonaws.connecthealth#ArtifactDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.error_message
    import aws_sdk_connecthealth.types.post_stream_artifact_generation_status
    import aws_sdk_connecthealth.types.uri


class ArtifactDetails(TypedDict, closed=True):
    output_location: NotRequired["aws_sdk_connecthealth.types.uri.Uri"]
    """<p/>"""
    status: NotRequired[
        "aws_sdk_connecthealth.types.post_stream_artifact_generation_status.PostStreamArtifactGenerationStatus"
    ]
    """<p>The generation status of the artifact</p>"""
    failure_reason: NotRequired[
        "aws_sdk_connecthealth.types.error_message.ErrorMessage"
    ]
    """<p>The reason for failure if the artifact generation failed</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactDetails) -> dict:
    out: dict = {}
    if "output_location" in value:
        out["outputLocation"] = value["output_location"]
    if "status" in value:
        import aws_sdk_connecthealth.types.post_stream_artifact_generation_status

        out["status"] = (
            aws_sdk_connecthealth.types.post_stream_artifact_generation_status.serialize_json(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> ArtifactDetails:
    out: ArtifactDetails = {}  # type: ignore[typeddict-item]
    if "outputLocation" in data:
        out["output_location"] = data["outputLocation"]
    if "status" in data:
        import aws_sdk_connecthealth.types.post_stream_artifact_generation_status

        out["status"] = (
            aws_sdk_connecthealth.types.post_stream_artifact_generation_status.deserialize_json(
                data["status"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
