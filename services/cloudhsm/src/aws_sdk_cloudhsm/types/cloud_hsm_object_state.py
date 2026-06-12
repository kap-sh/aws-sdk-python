"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CloudHsmObjectState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm.errors import DeserializationError

CloudHsmObjectState: TypeAlias = Literal[
    "READY",
    "UPDATING",
    "DEGRADED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "UPDATING",
        "DEGRADED",
    )
)


def serialize_aws_json_1_1(value: CloudHsmObjectState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudHsmObjectState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudHsmObjectState value: {data!r}")
    return cast(CloudHsmObjectState, data)
