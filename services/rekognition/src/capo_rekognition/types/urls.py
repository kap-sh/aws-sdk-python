"""Generated from Smithy shape ``com.amazonaws.rekognition#Urls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.url

Urls: TypeAlias = list["capo_rekognition.types.url.Url"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Urls) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Urls:
    return list(data)
