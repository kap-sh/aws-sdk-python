"""Generated from Smithy shape ``com.amazonaws.rekognition#RegionsOfInterest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.region_of_interest

RegionsOfInterest: TypeAlias = list[
    "capo_rekognition.types.region_of_interest.RegionOfInterest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionsOfInterest) -> list:
    import capo_rekognition.types.region_of_interest

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.region_of_interest.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegionsOfInterest:
    import capo_rekognition.types.region_of_interest

    out: RegionsOfInterest = []
    for item in data:
        out.append(
            capo_rekognition.types.region_of_interest.deserialize_aws_json_1_1(item)
        )
    return out
