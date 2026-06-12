"""Generated from Smithy shape ``com.amazonaws.transfer#AgreementStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

AgreementStatusType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: AgreementStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgreementStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgreementStatusType value: {data!r}")
    return cast(AgreementStatusType, data)
