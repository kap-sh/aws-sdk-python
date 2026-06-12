"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

SourceConnectorType: TypeAlias = Literal[
    "Salesforce",
    "Marketo",
    "Zendesk",
    "Servicenow",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Salesforce",
        "Marketo",
        "Zendesk",
        "Servicenow",
        "S3",
    )
)


def serialize_json(value: SourceConnectorType) -> str:
    return value


def deserialize_json(data: str) -> SourceConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceConnectorType value: {data!r}")
    return cast(SourceConnectorType, data)
