"""Generated from Smithy shape ``com.amazonaws.lightsail#TreatMissingData``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

TreatMissingData: TypeAlias = Literal[
    "breaching",
    "notBreaching",
    "ignore",
    "missing",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "breaching",
        "notBreaching",
        "ignore",
        "missing",
    )
)


def serialize_aws_json_1_1(value: TreatMissingData) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TreatMissingData:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TreatMissingData value: {data!r}")
    return cast(TreatMissingData, data)
