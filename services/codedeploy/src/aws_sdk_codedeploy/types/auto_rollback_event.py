"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoRollbackEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

AutoRollbackEvent: TypeAlias = Literal[
    "DEPLOYMENT_FAILURE",
    "DEPLOYMENT_STOP_ON_ALARM",
    "DEPLOYMENT_STOP_ON_REQUEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPLOYMENT_FAILURE",
        "DEPLOYMENT_STOP_ON_ALARM",
        "DEPLOYMENT_STOP_ON_REQUEST",
    )
)


def serialize_aws_json_1_1(value: AutoRollbackEvent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoRollbackEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoRollbackEvent value: {data!r}")
    return cast(AutoRollbackEvent, data)
