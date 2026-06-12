"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrackingServerSize: TypeAlias = Literal[
    "Small",
    "Medium",
    "Large",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Small",
        "Medium",
        "Large",
    )
)


def serialize_aws_json_1_1(value: TrackingServerSize) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrackingServerSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrackingServerSize value: {data!r}")
    return cast(TrackingServerSize, data)
