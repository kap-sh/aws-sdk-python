"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageFailureCode``."""

from typing import Literal, TypeAlias, cast

ImageFailureCode: TypeAlias = Literal[
    "InvalidImageDigest",
    "InvalidImageTag",
    "ImageTagDoesNotMatchDigest",
    "ImageNotFound",
    "MissingDigestAndTag",
    "ImageReferencedByManifestList",
    "KmsError",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageFailureCode:
    return cast(ImageFailureCode, data)
