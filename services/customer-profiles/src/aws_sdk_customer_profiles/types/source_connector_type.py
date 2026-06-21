"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceConnectorType``."""

from typing import Literal, TypeAlias, cast

SourceConnectorType: TypeAlias = Literal[
    "Salesforce",
    "Marketo",
    "Zendesk",
    "Servicenow",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceConnectorType) -> str:
    return value


def deserialize_json(data: str) -> SourceConnectorType:
    return cast(SourceConnectorType, data)
