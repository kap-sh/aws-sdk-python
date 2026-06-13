"""Generated from Smithy shape ``com.amazonaws.entityresolution#StatementPrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.statement_principal

StatementPrincipalList: TypeAlias = list[
    "aws_sdk_entityresolution.types.statement_principal.StatementPrincipal"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatementPrincipalList) -> list:
    return list(value)


def deserialize_json(data: list) -> StatementPrincipalList:
    return list(data)
