"""Generated from Smithy shape ``com.amazonaws.rekognition#VersionNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.version_name

VersionNames: TypeAlias = list["aws_sdk_rekognition.types.version_name.VersionName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VersionNames:
    return list(data)
