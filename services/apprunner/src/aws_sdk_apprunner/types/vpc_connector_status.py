"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcConnectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

VpcConnectorStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_0(value: VpcConnectorStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VpcConnectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcConnectorStatus value: {data!r}")
    return cast(VpcConnectorStatus, data)
