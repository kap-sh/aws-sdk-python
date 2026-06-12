"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

RevisionLocationType: TypeAlias = Literal[
    "S3",
    "GitHub",
    "String",
    "AppSpecContent",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "GitHub",
        "String",
        "AppSpecContent",
    )
)


def serialize_aws_json_1_1(value: RevisionLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RevisionLocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RevisionLocationType value: {data!r}")
    return cast(RevisionLocationType, data)
