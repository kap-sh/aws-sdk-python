"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

CedarVersion: TypeAlias = Literal[
    "CEDAR_2",
    "CEDAR_4",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CEDAR_2",
        "CEDAR_4",
    )
)


def serialize_aws_json_1_0(value: CedarVersion) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CedarVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CedarVersion value: {data!r}")
    return cast(CedarVersion, data)
