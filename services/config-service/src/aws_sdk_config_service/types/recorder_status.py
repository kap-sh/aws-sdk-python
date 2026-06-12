"""Generated from Smithy shape ``com.amazonaws.configservice#RecorderStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RecorderStatus: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failure",
    "NotApplicable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Success",
        "Failure",
        "NotApplicable",
    )
)


def serialize_aws_json_1_1(value: RecorderStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecorderStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecorderStatus value: {data!r}")
    return cast(RecorderStatus, data)
