"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.person_match

PersonMatches: TypeAlias = list["aws_sdk_rekognition.types.person_match.PersonMatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonMatches) -> list:
    import aws_sdk_rekognition.types.person_match

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.person_match.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PersonMatches:
    import aws_sdk_rekognition.types.person_match

    out: PersonMatches = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.person_match.deserialize_aws_json_1_1(item)
        )
    return out
