"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.s3_location


class AnalysisTemplateArtifact(TypedDict, closed=True):
    location: "aws_sdk_cleanrooms.types.s3_location.S3Location"
    """<p> The artifact location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateArtifact) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.s3_location

    out["location"] = aws_sdk_cleanrooms.types.s3_location.serialize_json(
        value["location"]
    )
    return out


def deserialize_json(data: dict) -> AnalysisTemplateArtifact:
    out: AnalysisTemplateArtifact = {}  # type: ignore[typeddict-item]
    if "location" in data:
        import aws_sdk_cleanrooms.types.s3_location

        out["location"] = aws_sdk_cleanrooms.types.s3_location.deserialize_json(
            data["location"]
        )
    else:
        raise DeserializationError("AnalysisTemplateArtifact.location required")
    return out
