"""Generated from Smithy shape ``com.amazonaws.rekognition#KnownGender``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.known_gender_type


class KnownGender(TypedDict):
    type: NotRequired["aws_sdk_rekognition.types.known_gender_type.KnownGenderType"]
    """<p>A string value of the KnownGender info about the Celebrity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KnownGender) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_rekognition.types.known_gender_type

        out["Type"] = (
            aws_sdk_rekognition.types.known_gender_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KnownGender:
    out: KnownGender = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.known_gender_type

        out["type"] = (
            aws_sdk_rekognition.types.known_gender_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
