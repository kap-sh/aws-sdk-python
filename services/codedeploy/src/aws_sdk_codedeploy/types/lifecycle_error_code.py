"""Generated from Smithy shape ``com.amazonaws.codedeploy#LifecycleErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

LifecycleErrorCode: TypeAlias = Literal[
    "Success",
    "ScriptMissing",
    "ScriptNotExecutable",
    "ScriptTimedOut",
    "ScriptFailed",
    "UnknownError",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "ScriptMissing",
        "ScriptNotExecutable",
        "ScriptTimedOut",
        "ScriptFailed",
        "UnknownError",
    )
)


def serialize_aws_json_1_1(value: LifecycleErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecycleErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecycleErrorCode value: {data!r}")
    return cast(LifecycleErrorCode, data)
