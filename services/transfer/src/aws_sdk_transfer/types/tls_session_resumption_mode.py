"""Generated from Smithy shape ``com.amazonaws.transfer#TlsSessionResumptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

TlsSessionResumptionMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "ENFORCED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "ENFORCED",
    )
)


def serialize_aws_json_1_1(value: TlsSessionResumptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TlsSessionResumptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TlsSessionResumptionMode value: {data!r}")
    return cast(TlsSessionResumptionMode, data)
