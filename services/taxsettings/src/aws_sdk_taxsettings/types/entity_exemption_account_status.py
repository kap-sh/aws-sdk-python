"""Generated from Smithy shape ``com.amazonaws.taxsettings#EntityExemptionAccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

EntityExemptionAccountStatus: TypeAlias = Literal[
    "None",
    "Valid",
    "Expired",
    "Pending",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Valid",
        "Expired",
        "Pending",
    )
)


def serialize_json(value: EntityExemptionAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> EntityExemptionAccountStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EntityExemptionAccountStatus value: {data!r}"
        )
    return cast(EntityExemptionAccountStatus, data)
