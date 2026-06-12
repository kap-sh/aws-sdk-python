"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LatestInferenceResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

LatestInferenceResult: TypeAlias = Literal[
    "ANOMALOUS",
    "NORMAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANOMALOUS",
        "NORMAL",
    )
)


def serialize_aws_json_1_0(value: LatestInferenceResult) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LatestInferenceResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LatestInferenceResult value: {data!r}")
    return cast(LatestInferenceResult, data)
