"""Generated from Smithy shape ``com.amazonaws.rekognition#ChallengePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.challenge_type
    import aws_sdk_rekognition.types.versions


class ChallengePreference(TypedDict, closed=True):
    type: "aws_sdk_rekognition.types.challenge_type.ChallengeType"
    """<p>The types of challenges that have been selected for the Face Liveness session.</p>"""
    versions: NotRequired["aws_sdk_rekognition.types.versions.Versions"]
    """<p>The version of the challenges that have been selected for the Face Liveness session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengePreference) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.challenge_type

    out["Type"] = aws_sdk_rekognition.types.challenge_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "versions" in value:
        import aws_sdk_rekognition.types.versions

        out["Versions"] = aws_sdk_rekognition.types.versions.serialize_aws_json_1_1(
            value["versions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChallengePreference:
    out: ChallengePreference = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.challenge_type

        out["type"] = aws_sdk_rekognition.types.challenge_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("ChallengePreference.type required")
    if "Versions" in data:
        import aws_sdk_rekognition.types.versions

        out["versions"] = aws_sdk_rekognition.types.versions.deserialize_aws_json_1_1(
            data["Versions"]
        )
    return out
