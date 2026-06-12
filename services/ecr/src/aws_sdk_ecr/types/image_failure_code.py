"""Generated from Smithy shape ``com.amazonaws.ecr#ImageFailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ImageFailureCode: TypeAlias = Literal[
    "InvalidImageDigest",
    "InvalidImageTag",
    "ImageTagDoesNotMatchDigest",
    "ImageNotFound",
    "MissingDigestAndTag",
    "ImageReferencedByManifestList",
    "KmsError",
    "UpstreamAccessDenied",
    "UpstreamTooManyRequests",
    "UpstreamUnavailable",
    "ImageInaccessible",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidImageDigest",
        "InvalidImageTag",
        "ImageTagDoesNotMatchDigest",
        "ImageNotFound",
        "MissingDigestAndTag",
        "ImageReferencedByManifestList",
        "KmsError",
        "UpstreamAccessDenied",
        "UpstreamTooManyRequests",
        "UpstreamUnavailable",
        "ImageInaccessible",
    )
)


def serialize_aws_json_1_1(value: ImageFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageFailureCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageFailureCode value: {data!r}")
    return cast(ImageFailureCode, data)
