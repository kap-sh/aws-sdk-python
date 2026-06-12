"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSQuotaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OpenZFSQuotaType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
    )
)


def serialize_aws_json_1_1(value: OpenZFSQuotaType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSQuotaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenZFSQuotaType value: {data!r}")
    return cast(OpenZFSQuotaType, data)
