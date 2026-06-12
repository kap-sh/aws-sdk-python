"""Generated from Smithy shape ``com.amazonaws.artifact#CustomerAgreementState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_artifact.errors import DeserializationError

CustomerAgreementState: TypeAlias = Literal[
    "ACTIVE",
    "CUSTOMER_TERMINATED",
    "AWS_TERMINATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CUSTOMER_TERMINATED",
        "AWS_TERMINATED",
    )
)


def serialize_json(value: CustomerAgreementState) -> str:
    return value


def deserialize_json(data: str) -> CustomerAgreementState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerAgreementState value: {data!r}")
    return cast(CustomerAgreementState, data)
