"""Generated from Smithy shape ``com.amazonaws.sagemaker#ThroughputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ThroughputMode: TypeAlias = Literal[
    "OnDemand",
    "Provisioned",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OnDemand",
        "Provisioned",
    )
)


def serialize_aws_json_1_1(value: ThroughputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThroughputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThroughputMode value: {data!r}")
    return cast(ThroughputMode, data)
