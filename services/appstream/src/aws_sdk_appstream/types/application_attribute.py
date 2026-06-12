"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ApplicationAttribute: TypeAlias = Literal[
    "LAUNCH_PARAMETERS",
    "WORKING_DIRECTORY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LAUNCH_PARAMETERS",
        "WORKING_DIRECTORY",
    )
)


def serialize_aws_json_1_1(value: ApplicationAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationAttribute value: {data!r}")
    return cast(ApplicationAttribute, data)
