"""Generated from Smithy shape ``com.amazonaws.codebuild#LanguageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

LanguageType: TypeAlias = Literal[
    "JAVA",
    "PYTHON",
    "NODE_JS",
    "RUBY",
    "GOLANG",
    "DOCKER",
    "ANDROID",
    "DOTNET",
    "BASE",
    "PHP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JAVA",
        "PYTHON",
        "NODE_JS",
        "RUBY",
        "GOLANG",
        "DOCKER",
        "ANDROID",
        "DOTNET",
        "BASE",
        "PHP",
    )
)


def serialize_aws_json_1_1(value: LanguageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LanguageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageType value: {data!r}")
    return cast(LanguageType, data)
