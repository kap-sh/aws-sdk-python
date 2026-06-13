"""Generated from Smithy shape ``com.amazonaws.odb#ComputeModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

ComputeModel: TypeAlias = Literal[
    "ECPU",
    "OCPU",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ECPU",
        "OCPU",
    )
)


def serialize_aws_json_1_0(value: ComputeModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComputeModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeModel value: {data!r}")
    return cast(ComputeModel, data)
