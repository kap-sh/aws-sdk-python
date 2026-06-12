"""Generated from Smithy shape ``com.amazonaws.ecr#SubjectIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_digest


class SubjectIdentifier(TypedDict):
    image_digest: "aws_sdk_ecr.types.image_digest.ImageDigest"
    """<p>The digest of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectIdentifier) -> dict:
    out: dict = {}
    out["imageDigest"] = value["image_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubjectIdentifier:
    out: SubjectIdentifier = {}  # type: ignore[typeddict-item]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    else:
        raise DeserializationError("SubjectIdentifier.image_digest required")
    return out
