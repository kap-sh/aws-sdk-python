"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetStatusMessageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

DatasetStatusMessageCode: TypeAlias = Literal[
    "SUCCESS",
    "SERVICE_ERROR",
    "CLIENT_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "SERVICE_ERROR",
        "CLIENT_ERROR",
    )
)


def serialize_aws_json_1_1(value: DatasetStatusMessageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetStatusMessageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatusMessageCode value: {data!r}")
    return cast(DatasetStatusMessageCode, data)
