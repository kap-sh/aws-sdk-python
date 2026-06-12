"""Generated from Smithy shape ``com.amazonaws.rekognition#Challenge``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.challenge_type
    import aws_sdk_rekognition.types.version


class Challenge(TypedDict):
    type: "aws_sdk_rekognition.types.challenge_type.ChallengeType"
    """<p>The type of the challenge being used for the Face Liveness session.</p>"""
    version: "aws_sdk_rekognition.types.version.Version"
    """<p>The version of the challenge being used for the Face Liveness session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Challenge) -> dict:
    out: dict = {}
    import aws_sdk_rekognition.types.challenge_type

    out["Type"] = aws_sdk_rekognition.types.challenge_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Challenge:
    out: Challenge = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.challenge_type

        out["type"] = aws_sdk_rekognition.types.challenge_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("Challenge.type required")
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("Challenge.version required")
    return out
