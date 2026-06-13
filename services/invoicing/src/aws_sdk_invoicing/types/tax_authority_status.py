"""Generated from Smithy shape ``com.amazonaws.invoicing#TaxAuthorityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

TaxAuthorityStatus: TypeAlias = Literal[
    "ISSUED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ISSUED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_0(value: TaxAuthorityStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaxAuthorityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaxAuthorityStatus value: {data!r}")
    return cast(TaxAuthorityStatus, data)
