"""Generated from Smithy shape ``com.amazonaws.sagemaker#PreemptTeamTasks``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

PreemptTeamTasks: TypeAlias = Literal[
    "Never",
    "LowerPriority",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Never",
        "LowerPriority",
    )
)


def serialize_aws_json_1_1(value: PreemptTeamTasks) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreemptTeamTasks:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreemptTeamTasks value: {data!r}")
    return cast(PreemptTeamTasks, data)
