"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

TaxRegistrationStatus: TypeAlias = Literal[
    "Verified",
    "Pending",
    "Deleted",
    "Rejected",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Verified",
        "Pending",
        "Deleted",
        "Rejected",
    )
)


def serialize_json(value: TaxRegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaxRegistrationStatus value: {data!r}")
    return cast(TaxRegistrationStatus, data)
