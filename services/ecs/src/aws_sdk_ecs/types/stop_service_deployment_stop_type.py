"""Generated from Smithy shape ``com.amazonaws.ecs#StopServiceDeploymentStopType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

StopServiceDeploymentStopType: TypeAlias = Literal[
    "ABORT",
    "ROLLBACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ABORT",
        "ROLLBACK",
    )
)


def serialize_aws_json_1_1(value: StopServiceDeploymentStopType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopServiceDeploymentStopType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StopServiceDeploymentStopType value: {data!r}"
        )
    return cast(StopServiceDeploymentStopType, data)
