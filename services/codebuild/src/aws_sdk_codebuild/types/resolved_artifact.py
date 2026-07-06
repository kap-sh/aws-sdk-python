"""Generated from Smithy shape ``com.amazonaws.codebuild#ResolvedArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.artifacts_type
    import aws_sdk_codebuild.types.string


class ResolvedArtifact(TypedDict, closed=True):
    type: NotRequired["aws_sdk_codebuild.types.artifacts_type.ArtifactsType"]
    """<p>Specifies the type of artifact.</p>"""
    location: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The location of the artifact.</p>"""
    identifier: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The identifier of the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedArtifact) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_codebuild.types.artifacts_type

        out["type"] = aws_sdk_codebuild.types.artifacts_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedArtifact:
    out: ResolvedArtifact = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_codebuild.types.artifacts_type

        out["type"] = aws_sdk_codebuild.types.artifacts_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "location" in data:
        out["location"] = data["location"]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    return out
