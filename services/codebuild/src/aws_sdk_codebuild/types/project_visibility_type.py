"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectVisibilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

"""<p>Specifies the visibility of the project's builds. Possible values are:</p> <dl> <dt>PUBLIC_READ</dt> <dd> <p>The project builds are visible to the public.</p> </dd> <dt>PRIVATE</dt> <dd> <p>The project builds are not visible to the public.</p> </dd> </dl>"""
ProjectVisibilityType: TypeAlias = Literal[
    "PUBLIC_READ",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC_READ",
        "PRIVATE",
    )
)


def serialize_aws_json_1_1(value: ProjectVisibilityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectVisibilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectVisibilityType value: {data!r}")
    return cast(ProjectVisibilityType, data)
