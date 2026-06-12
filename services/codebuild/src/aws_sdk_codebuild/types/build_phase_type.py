"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildPhaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

BuildPhaseType: TypeAlias = Literal[
    "SUBMITTED",
    "QUEUED",
    "PROVISIONING",
    "DOWNLOAD_SOURCE",
    "INSTALL",
    "PRE_BUILD",
    "BUILD",
    "POST_BUILD",
    "UPLOAD_ARTIFACTS",
    "FINALIZING",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "QUEUED",
        "PROVISIONING",
        "DOWNLOAD_SOURCE",
        "INSTALL",
        "PRE_BUILD",
        "BUILD",
        "POST_BUILD",
        "UPLOAD_ARTIFACTS",
        "FINALIZING",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: BuildPhaseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BuildPhaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuildPhaseType value: {data!r}")
    return cast(BuildPhaseType, data)
