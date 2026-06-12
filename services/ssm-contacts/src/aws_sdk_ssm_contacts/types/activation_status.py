"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ActivationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_contacts.errors import DeserializationError

ActivationStatus: TypeAlias = Literal[
    "ACTIVATED",
    "NOT_ACTIVATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATED",
        "NOT_ACTIVATED",
    )
)


def serialize_aws_json_1_1(value: ActivationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActivationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActivationStatus value: {data!r}")
    return cast(ActivationStatus, data)
