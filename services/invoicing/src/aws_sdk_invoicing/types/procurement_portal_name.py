"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

ProcurementPortalName: TypeAlias = Literal[
    "SAP_BUSINESS_NETWORK",
    "COUPA",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAP_BUSINESS_NETWORK",
        "COUPA",
    )
)


def serialize_aws_json_1_0(value: ProcurementPortalName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProcurementPortalName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcurementPortalName value: {data!r}")
    return cast(ProcurementPortalName, data)
