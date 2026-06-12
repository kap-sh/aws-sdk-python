"""Generated from Smithy shape ``com.amazonaws.codedeploy#BundleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

BundleType: TypeAlias = Literal[
    "tar",
    "tgz",
    "zip",
    "YAML",
    "JSON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "tar",
        "tgz",
        "zip",
        "YAML",
        "JSON",
    )
)


def serialize_aws_json_1_1(value: BundleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BundleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BundleType value: {data!r}")
    return cast(BundleType, data)
