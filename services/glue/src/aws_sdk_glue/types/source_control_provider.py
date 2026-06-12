"""Generated from Smithy shape ``com.amazonaws.glue#SourceControlProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SourceControlProvider: TypeAlias = Literal[
    "GITHUB",
    "GITLAB",
    "BITBUCKET",
    "AWS_CODE_COMMIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GITHUB",
        "GITLAB",
        "BITBUCKET",
        "AWS_CODE_COMMIT",
    )
)


def serialize_aws_json_1_1(value: SourceControlProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceControlProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceControlProvider value: {data!r}")
    return cast(SourceControlProvider, data)
