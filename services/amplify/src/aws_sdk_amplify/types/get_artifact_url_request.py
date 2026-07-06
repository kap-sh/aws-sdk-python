"""Generated from Smithy shape ``com.amazonaws.amplify#GetArtifactUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplify.types.artifact_id


class GetArtifactUrlRequest(TypedDict, closed=True):
    artifact_id: "aws_sdk_amplify.types.artifact_id.ArtifactId"
    """<p>The unique ID for an artifact. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArtifactUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetArtifactUrlRequest:
    out: GetArtifactUrlRequest = {}  # type: ignore[typeddict-item]
    return out
