"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentEnrichmentConditionOperator``."""

from typing import Literal, TypeAlias, cast

DocumentEnrichmentConditionOperator: TypeAlias = Literal[
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
    "EQUALS",
    "NOT_EQUALS",
    "CONTAINS",
    "NOT_CONTAINS",
    "EXISTS",
    "NOT_EXISTS",
    "BEGINS_WITH",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentEnrichmentConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> DocumentEnrichmentConditionOperator:
    return cast(DocumentEnrichmentConditionOperator, data)
