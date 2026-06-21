"""Generated from Smithy shape ``com.amazonaws.appflow#InforNexusConnectorOperator``."""

from typing import Literal, TypeAlias, cast

InforNexusConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "BETWEEN",
    "EQUAL_TO",
    "ADDITION",
    "MULTIPLICATION",
    "DIVISION",
    "SUBTRACTION",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NUMERIC",
    "NO_OP",
]


# --- restJson1 ser/de ---
def serialize_json(value: InforNexusConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> InforNexusConnectorOperator:
    return cast(InforNexusConnectorOperator, data)
